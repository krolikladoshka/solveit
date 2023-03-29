use std::{cmp::{min}, collections::VecDeque};
use std::path::Path;
use rand::{self, Rng};

const DEFAULT_CPU_SPEED: u32 = 700;
const DEFAULT_POINTER_START: usize = 0x200;
const DEFAULT_INDEX_REGISTER_START: usize = 0x50;
const INSTRUCTION_SIZE: usize = 2;
const TIMER_COUNTDOWN_RATE_PER_SECOND: u8 = 60;
const REGISTERS_COUNT: usize = 16;
const MEMORY_SIZE: usize = 4096;
const STACK_SIZE: usize = 1024;
const KEYS_COUNT: usize = 16;

pub const DISPLAY_WIDTH: usize = 64;
pub const DISPLAY_HEIGHT: usize = 32;
pub const DISPLAY_SIZE: usize = DISPLAY_WIDTH * DISPLAY_HEIGHT;


const DEFAULT_FONT: [u8; 80] = [
    0xF0, 0x90, 0x90, 0x90, 0xF0, // 0
    0x20, 0x60, 0x20, 0x20, 0x70, // 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0, // 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0, // 3
    0x90, 0x90, 0xF0, 0x10, 0x10, // 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0, // 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0, // 6
    0xF0, 0x10, 0x20, 0x40, 0x40, // 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0, // 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0, // 9
    0xF0, 0x90, 0xF0, 0x90, 0x90, // A
    0xE0, 0x90, 0xE0, 0x90, 0xE0, // B
    0xF0, 0x80, 0x80, 0x80, 0xF0, // C
    0xE0, 0x90, 0x90, 0x90, 0xE0, // D
    0xF0, 0x80, 0xF0, 0x80, 0xF0, // E
    0xF0, 0x80, 0xF0, 0x80, 0x80  // F
];

pub struct Chip8 {
    pub pointer: usize,
    pub i: usize,
    delay_timer: u8,
    sound_timer: u8,
    pub registers: [u8; REGISTERS_COUNT],
    pub stack: VecDeque<usize>,
    pub memory: [u8; MEMORY_SIZE],
    pub canvas: [[u8; DISPLAY_WIDTH]; DISPLAY_HEIGHT],
    pub speed: u32,
}

impl Chip8 {
    pub fn new() -> Self {
        let mut chip8 = Chip8 {
            pointer: DEFAULT_POINTER_START,
            i: DEFAULT_INDEX_REGISTER_START,
            delay_timer: 0,
            sound_timer: 0,
            registers: [0; REGISTERS_COUNT],
            stack: VecDeque::with_capacity(STACK_SIZE / 4),
            speed: DEFAULT_CPU_SPEED,
            memory: [0; MEMORY_SIZE],
            canvas: [[0; DISPLAY_WIDTH]; DISPLAY_HEIGHT],
        };

        chip8.load_font();

        return chip8;
    }

    pub fn load_program(&mut self, path: &Path) {
        match std::fs::read(path) {
            Ok(bytes) => {
                let slice_size = bytes.len();

                if slice_size > (MEMORY_SIZE - 0x200) {
                    panic!("ch8 rom file is too big, file {}, size {}", path.as_os_str().to_str().unwrap(), slice_size);
                }
                self.memory[0x200..0x200 + slice_size].copy_from_slice(&bytes)
            },
            Err(e) => panic!("{}", e),
        }
    }

    pub fn load_font(&mut self) {
        let start_address = 0x50;
        
        self.memory[start_address..start_address + DEFAULT_FONT.len()].copy_from_slice(&DEFAULT_FONT);
    }

    pub fn new_with_cpu_speed(instructions_per_second: u32) -> Self {
        let mut new = Self::new();

        new.speed = instructions_per_second;

        return new;
    }

    pub fn fetch_opcode(&self) -> u16 {
        let opcode = (
            (self.memory[self.pointer] as u16) << 8) |
            ((self.memory[self.pointer + 1] as u16)
        );

        return opcode;
    }

    pub fn cycle(&mut self) {
        let sixty_hertz = self.speed / TIMER_COUNTDOWN_RATE_PER_SECOND as u32;
        
        for i in 0..1 {
            if i % sixty_hertz == 0 {
                if self.delay_timer > 0 {
                    self.delay_timer -= 1;
                }
                if self.sound_timer > 0 {
                    self.sound_timer -= 1;
                }                
            }
            
            let opcode = self.fetch_opcode();
            self.pointer += INSTRUCTION_SIZE;
           
            self.execute_next(opcode);
        }
    }
    
    fn clear_screen(&mut self) {
        self.canvas = [[0; DISPLAY_WIDTH]; DISPLAY_HEIGHT];
    }

    fn draw(&mut self, start_x: usize, start_y: usize, sprite_height: usize) {
        self.registers[0xF] = 0;

        let mut start_x = start_x % DISPLAY_WIDTH;
        let mut start_y = start_y % DISPLAY_HEIGHT;
        
        let y_boundary = min(start_y + sprite_height, DISPLAY_HEIGHT);
        let x_boundary = min(start_x + 8, DISPLAY_WIDTH);
        
        for y in start_y..y_boundary {
            let sprite_byte = self.memory[self.i + (y - start_y)];
            let mut offset = 7;

            for x in start_x..x_boundary {
                let bit = (sprite_byte >> offset) & 1;
                offset -= 1;

                if bit == 0 {
                    continue;
                }

                if self.canvas[y][x] == 1 {
                    self.canvas[y][x] = 0;
                    self.registers[0xF] = 1;
                } else {
                    self.canvas[y][x] = 1;
                }
            }
        }
    }

    fn execute_next(&mut self, opcode: u16) {
        /*
        implemented:
            00E0 (clear screen)
            1NNN (jump)
            6XNN (set register VX)
            7XNN (add value to register VX)
            ANNN (set index register I)
            DXYN (display/draw)
            00EE and 2NNN: Subroutines


         */
        let first_nibble = (opcode >> 12) as u8;
        let second_nibble = ((opcode >> 8) & 0xF) as u8;
        let third_nibble = ((opcode >> 4) & 0xF) as u8;
        let argument = (opcode & 0xF) as u8;
        let x_register = second_nibble as usize;
        let y_register = third_nibble as usize;

        let byte_arg = (third_nibble << 4) | argument;
        let long_byte_arg = ((second_nibble as u16) << 8)| (third_nibble << 4) as u16 | argument as u16;

        match first_nibble {
            0x0 => {
                if opcode & 0xFFF == 0 {
                    panic!("Jump is not implemented");
                } else {
                    match byte_arg {
                        0xE0 => self.clear_screen(),
                        0xEE => self.pointer = self.stack.pop_back().unwrap(),
                        _ => panic!("Unknown 0x0XXX opcode"),
                    }
                }
            },
            // + skips & jumps
            0x1 => self.pointer = long_byte_arg as usize,
            0x2 => {
                self.stack.push_back(self.pointer);
                self.pointer = long_byte_arg as usize;
            },
            0x3 => {
                if self.registers[x_register] == byte_arg {
                    self.pointer += INSTRUCTION_SIZE;
                }
            },
            0x4 => {
                if self.registers[x_register] != byte_arg {
                    self.pointer += INSTRUCTION_SIZE;
                }
            },
            0x5 => {
                if self.registers[x_register] == self.registers[y_register] {
                    self.pointer += INSTRUCTION_SIZE;
                }
            },
            0x9 => {
                if self.registers[x_register] != self.registers[y_register] {
                    self.pointer += INSTRUCTION_SIZE;
                }
            },
            // - skips and
            // + logic & arithmetic
            0x8 => {
                match argument {
                    0x0 => self.registers[x_register] = self.registers[y_register],
                    0x1 => self.registers[x_register] |= self.registers[y_register],
                    0x2 => self.registers[x_register] &= self.registers[y_register],
                    0x3 => self.registers[x_register] ^= self.registers[y_register],
                    0x4 => {
                        let (result, overflow) = self.registers[x_register].overflowing_add(
                            self.registers[y_register]
                        );
                        self.registers[x_register] = result;
                        
                        if overflow {
                            self.registers[0xF] = 1;
                        } else {
                            self.registers[0xF] = 0;
                        }
                    },
                    0x5 => {
                        let vx = self.registers[x_register];
                        let vy = self.registers[y_register];
                        
                        if vy <= vx {
                            self.registers[0xF] = 1;
                        } else {
                            self.registers[0xF] = 0;
                        }
                        
                        self.registers[x_register] = vx.wrapping_sub(vy);
                    },
                    0x7 => {
                        let vx = self.registers[x_register];
                        let vy = self.registers[y_register];
                        
                        if vx <= vy {
                            self.registers[0xF] = 1;
                        } else {
                            self.registers[0xF] = 0;
                        }
                        
                        self.registers[x_register] = vy.wrapping_sub(vx);

                    },
                    0x6 => {
                        self.registers[x_register] = self.registers[y_register];
                        self.registers[0xF] = self.registers[x_register] & 1;
                        self.registers[x_register] >>= 1;
                    },
                    0xE => {
                        self.registers[x_register] = self.registers[y_register];
                        self.registers[0xF] = self.registers[x_register] & 1;
                        self.registers[x_register] = self.registers[x_register].wrapping_shl(1);
                    },
                    _ => {}
                }
            } 
            // - logic & arithmetic
            0x6 => {
                self.registers[x_register] = byte_arg as u8;
            },
            0x7 => {
                self.registers[x_register] = self.registers[x_register].wrapping_add(byte_arg as u8);
            },
            0xA => {
                self.i = long_byte_arg as usize;
            },
            0xB => {
                self.pointer = (long_byte_arg + self.registers[0] as u16) as usize;
            },
            0xC => {
                self.registers[x_register] = (rand::thread_rng().gen_range(0..1024) | 0xFF) as u8;
            },
            0xD => {
                self.draw(
                    self.registers[x_register] as usize,
                    self.registers[y_register] as usize,
                    argument as usize
                );
            }
            _ => panic!("Unknown opcode")
        };
    }
}
