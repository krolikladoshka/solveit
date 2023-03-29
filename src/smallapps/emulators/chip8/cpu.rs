use std::cmp::{min ,max};

const DEFAULT_CPU_SPEED: u32 = 700;
const DEFAULT_POINTER_START: u16 = 200;
const INSTRUCTION_SIZE: u16 = 2;
const TIMER_COUNTDOWN_RATE_PER_SECOND: u8 = 60;
const REGISTERS_COUNT: usize = 16;
const MEMORY_SIZE: usize = 4096;
const DISPLAY_WIDTH: usize = 64;
const DISPLAY_HEIGHT: usize = 32;
const DISPLAY_SIZE: usize = DISPLAY_WIDTH * DISPLAY_HEIGHT;


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

pub struct CPU {
    pub pointer: u16,
    pub i: u16,
    delay_timer: u8,
    sound_timer: u8,
    pub registers: [u8; REGISTERS_COUNT],
    pub speed: u32,
    pub memory: [u8; MEMORY_SIZE],
}

impl CPU {
    pub fn new() -> Self {
        return CPU {
            pointer: DEFAULT_POINTER_START,
            i: DEFAULT_POINTER_START,
            delay_timer: 0,
            sound_timer: 0,
            registers: [0; REGISTERS_COUNT],
            speed: DEFAULT_CPU_SPEED,
            memory: [0; MEMORY_SIZE],
        };
    }

    pub fn new_with_cpu_speed(instructions_per_second: u32) -> Self {
        let mut new = Self::new();

        new.speed = instructions_per_second;

        return new;
    }

    pub fn cycle(&mut self) {
        let sixty_hertz = self.speed / TIMER_COUNTDOWN_RATE_PER_SECOND as u32;
        
        for i in 0..self.speed {
            if i % sixty_hertz == 0 {
                self.delay_timer = max(0, self.delay_timer - 1);
                self.sound_timer = max(0, self.sound_timer - 1);
            }
           
            self.execute_next();
            self.pointer += INSTRUCTION_SIZE;
        }
    }

    fn execute_next(&self) {
    }
}


pub struct Display {
    pub canvas: [u8; DISPLAY_SIZE]
}

impl Display {
    pub fn new() -> Self {
        return Display {
            canvas: [0; DISPLAY_SIZE],
        };
    }
}

pub struct Chip8 {
    pub cpu: CPU,
    pub display: Display,
}

impl Chip8 {
    pub fn new() -> Self {
        let mut chip8 = Chip8 {
            cpu: CPU::new(),
            display: Display::new(),
        };
        
        chip8.load_font();

        return chip8;
    }

    pub fn load_font(&mut self) {
        let start_address = 0x50;
        
        self.cpu.memory[start_address..].copy_from_slice(&DEFAULT_FONT);
    }
}