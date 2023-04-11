pub mod registers;

use std::{cell::RefCell, rc::Rc};

use log::{warn, error, debug};

use self::registers::{Controller, Mask, Status, Scroll, LoopyRegister};

use super::cartridge::{Cartridge, Mirroring};

pub const SCANLINES_COUNT: i32 = 262;
pub const SCANLINES_PER_FRAME: i32 = 241;
pub const CYCLES_TO_DRAW_SCANLINE: usize = 341;
pub const VISIBLE_SCANLINE_CYCLES: usize = 256;
pub const PPU_MEMORY_SIZE: usize = 0x800;
pub const OAM_DATA_SIZE: usize = 0x100;
pub const PALETTE_TABLE_SIZE: usize = 32;

pub const PALETTE_MEMORY_START: u16 = 0x3F00;
pub const ATTRIBUTE_MEMORY_OFFSET: u16 = 0x03C0;

pub const CHR_ROM_PAGE_START: u16 = 0x0000;
pub const CHR_ROM_PAGE_END: u16 = 0x1FFF;
pub const VRAM_PAGE_START: u16 = 0x2000;
pub const VRAM_PAGE_END: u16 = 0x3EFF;
pub const PALETTE_PAGE_START: u16 = 0x3F00;
pub const PALETTE_PAGE_END: u16 = 0x3FFF;
pub const PALETTE_INTERNAL_MIRRORS: [usize; 4] = [
    0x10, 0x14, 0x18, 0x1C,
];

pub const NAMETABLE_MIRROR_MASK: u16 = 0xFFF;

pub const SCREEN_WIDTH: usize = 256;
pub const SCREEN_HEIGHT: usize = 240;

pub const PALETTE: [[u8; 3]; 64] = [
    [84, 84, 84],
    [0, 30, 116],
    [8, 16, 144],
    [48, 0, 136],
    [68, 0, 100],
    [92, 0, 48],
    [84, 4, 0],
    [60, 24, 0],
    [32, 42, 0],
    [8, 58, 0],
    [0, 64, 0],
    [0, 60, 0],
    [0, 50, 60],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [152, 150, 152],
    [8, 76, 196],
    [48, 50, 236],
    [92, 30, 228],
    [136, 20, 176],
    [160, 20, 100],
    [152, 34, 32],
    [120, 60, 0],
    [84, 90, 0],
    [40, 114, 0],
    [8, 124, 0],
    [0, 118, 40],
    [0, 102, 120],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [236, 238, 236],
    [76, 154, 236],
    [120, 124, 236],
    [176, 98, 236],
    [228, 84, 236],
    [236, 88, 180],
    [236, 106, 100],
    [212, 136, 32],
    [160, 170, 0],
    [116, 196, 0],
    [76, 208, 32],
    [56, 204, 108],
    [56, 180, 204],
    [60, 60, 60],
    [0, 0, 0],
    [0, 0, 0],
    [236, 238, 236],
    [168, 204, 236],
    [188, 188, 236],
    [212, 178, 236],
    [236, 174, 236],
    [236, 174, 212],
    [236, 180, 176],
    [228, 196, 144],
    [204, 210, 120],
    [180, 222, 120],
    [168, 226, 144],
    [152, 226, 180],
    [160, 214, 228],
    [160, 162, 160],
    [0, 0, 0],
    [0, 0, 0],
];

pub struct PPU {
    pub total_cycles: usize,
    pub cycles: usize,
    pub nmi_interrupt: bool,

    pub latch: bool,
    pub control_register: Controller,
    pub mask_register: Mask,
    pub status_register: Status,
    pub oam_address_register: u8,
    pub oam_data_register: u8,
    
    pub address_register: LoopyRegister,
    pub temp_address_register: LoopyRegister, 
    fine_x: u8,

    next_background_tile_id: u8,
    next_background_tile_attribute: u8,
    next_background_tile_lsb: u8,
    next_background_tile_msb: u8, 
    background_shifter_pattern_low: u16,
    background_shifter_pattern_high: u16,
    background_shifter_attribute_low: u16,
    background_shifter_attribute_high: u16,
    
    pub screen: [[u8; SCREEN_WIDTH]; SCREEN_HEIGHT],

    pub data_buffer: u8, 

    pub memory: [u8; PPU_MEMORY_SIZE],
    pub oam_data: [u8; OAM_DATA_SIZE],
    pub palette: [u8; PALETTE_TABLE_SIZE],

    pub debug_pattern_tables: [[[u8; 128]; 128];2],

    pub cartridge: Rc<RefCell<Cartridge>>,

    pub scanlines: i32,
    // pub mirroring: Mirroring,

    pub completed_frame: bool,
    pub odd_frame: bool,
}

impl PPU {
    pub fn new(cartridge: Rc<RefCell<Cartridge>>) -> Self {
        let mut ppu = PPU {
            total_cycles: 0,
            cycles: 0,
            nmi_interrupt: false,
            latch: false,
            control_register: Controller::empty(),
            // mask_register: Mask::from_bits_truncate(0b00011110),
            mask_register: Mask::empty(),
            status_register: Status::empty(),
            oam_address_register: 0,
            oam_data_register: 0,
            address_register: LoopyRegister::new(),
            temp_address_register: LoopyRegister::new(),
            fine_x: 0,
            next_background_tile_id: 0,
            next_background_tile_attribute: 0,
            next_background_tile_lsb: 0,
            next_background_tile_msb: 0, 
            background_shifter_pattern_low: 0,
            background_shifter_pattern_high: 0,
            background_shifter_attribute_low: 0,
            background_shifter_attribute_high: 0,
            screen: [[0; SCREEN_WIDTH]; SCREEN_HEIGHT],
            data_buffer: 0,
            memory: [0; PPU_MEMORY_SIZE],
            oam_data: [0; OAM_DATA_SIZE],
            palette: [0; PALETTE_TABLE_SIZE],
            debug_pattern_tables: [[[0; 128]; 128];2],
            cartridge: cartridge,
            scanlines: 0,
            completed_frame: false,
            odd_frame: false,
        };

        return ppu;
    }

    pub fn draw_pattern_tables(&mut self) {
        for i in 0..self.debug_pattern_tables.len() {
            for y in 0..16 {
                for x in 0..16 {
                    let offset = y * 256 + x * 16;

                    for row in 0..8 {
                        let mut tile_lsb = self.read_u8((i * 0x1000 + offset + row) as u16);
                        let mut tile_msb = self.read_u8((i * 0x1000 + offset + row + 8) as u16);

                        for col in 0..8 {
                            let pixel = ((tile_msb & 0x01) << 1) | (tile_lsb & 0x1);
                            
                            tile_lsb >>= 1;
                            tile_msb >>= 1;
                            
                            let color = self.read_u8(
                                PALETTE_MEMORY_START + (0 << 2) as u16 + pixel as u16
                            );
                            self.debug_pattern_tables[i][y * 8 + row][x * 8 + (7 - col)] = color;
                        }
                    }
                }
            }
        }
    }

    /* +register reads */
    pub fn read_status_register(&mut self) -> u8 {
        let result = self.status_register.read(self.data_buffer);
        
        self.status_register.remove(Status::VERTICAL_BLANK);
        self.latch = false;

        return result;
    }

    pub fn read_oam_data_register(&self) -> u8 {
        return self.oam_data[self.oam_address_register as usize];
    }

    pub fn read_data_register(&mut self) -> u8 {
        let mut result = self.data_buffer;
        let address = self.address_register.address();
        
        self.data_buffer = self.read_u8(address);

        if address >= PALETTE_PAGE_START {
            result = self.data_buffer;
        }

        self.increment_address_register();
        
        return result;
    }
    /* -register reads */

    /* +register writes */
    pub fn write_control_register(&mut self, value: u8) {
        self.control_register = Controller::from_bits(value).unwrap();

        if self.control_register.contains(Controller::NAMETABLE_X) {
            self.temp_address_register.nametable_x = 1
        } else {
            self.temp_address_register.nametable_x = 0;
        }

        if self.control_register.contains(Controller::NAMETABLE_Y) {
            self.temp_address_register.nametable_y = 1
        } else {
            self.temp_address_register.nametable_y = 0;
        }
    }

    pub fn write_mask_register(&mut self, value: u8) {
        self.mask_register = Mask::from_bits(value).unwrap();
    }

    pub fn write_oam_address_register(&mut self, value: u8) {
        self.oam_address_register = value;
    }

    pub fn write_oam_data_register(&mut self, value: u8) {
        self.oam_data_register = value;
        self.oam_data[self.oam_address_register as usize] = value;
        self.oam_address_register = self.oam_address_register.wrapping_add(1);
    }

    pub fn write_scroll_register(&mut self, value: u8) {
        if !self.latch {
            self.fine_x = value & 0x7;
            self.temp_address_register.set_coarse_x(value >> 3);
            
            self.latch = true;
        } else {
            self.address_register.set_fine_y(value & 0x7);
            self.temp_address_register.set_coarse_y(value >> 3);

            self.latch = false;
        }
    }

    pub fn write_address_register(&mut self, value: u8) {
        if !self.latch {
            let mut address = self.temp_address_register.address();
            address = ((value as u16 & 0x3F) << 8) | (address & 0xFF);
        
            self.temp_address_register.set(address);

            self.latch = true;
        } else {
            let mut address = self.temp_address_register.address();
            address = (address & 0xFF00) | (value as u16);
            
            self.temp_address_register.set(address);
            self.address_register.set(address);
            
            self.latch = false;
        }
    }

    pub fn write_data_register(&mut self, value: u8) {
        let address = self.address_register.address();
        
        self.write_u8(address, value);

        self.increment_address_register();
    }

    pub fn write_oam_dma_register_seq(&mut self, value: u8) {
        self.write_oam_data_register(value);
    }
    /* -register writes */

    pub fn increment_address_register(&mut self) {
        let vertical_mode = self.control_register.contains(Controller::VRAM_ADDRESS_INCREMENT);

        self.address_register.increment(vertical_mode);
    }

    fn read_from_internal_memory(&mut self, address: usize) -> u8 {
        let mirrored_address = address & (NAMETABLE_MIRROR_MASK as usize);
        let name_table_index = mirrored_address / PPU_MEMORY_SIZE;
        let mirroring = self.cartridge.borrow_mut().mirroring;

        match mirroring {
            Mirroring::Horizontal => {
                match mirrored_address {
                    0x000..=0x3FF | 0x400..=0x7FF => {
                        return self.memory[mirrored_address & (PPU_MEMORY_SIZE - 1)];
                    },
                    0x800..=0xBff | 0xC00..=0xFFF => {
                        return self.memory[(mirrored_address & (PPU_MEMORY_SIZE - 1))];
                    },
                    _ => {
                        error!(
                            "Attempt to read from wrong mirrored address: {:X}; {:X}; {:?}",
                            address, mirrored_address, mirroring
                        );
                        panic!(
                            "Attempt to read from wrong mirrored address: {:X}; {:X}; {:?}",
                            address, mirrored_address, mirroring
                        );
                    }
                }
            },
            Mirroring::Vertical => {
                match mirrored_address {
                    0x000..=0x3FF | 0x800..=0xBff  => {
                        return self.memory[mirrored_address & (PPU_MEMORY_SIZE - 1)];
                    },
                    0x400..=0x7FF | 0xC00..=0xFFF => {
                        return self.memory[PPU_MEMORY_SIZE + (mirrored_address & (PPU_MEMORY_SIZE - 1))];
                    },
                    _ => {
                        error!(
                            "Attempt to read from wrong mirrored address: {:X}; {:X}; {:?}",
                            address, mirrored_address, mirroring
                        );
                        panic!(
                            "Attempt to read from wrong mirrored address: {:X}; {:X}; {:?}",
                            address, mirrored_address, mirroring
                        );
                    }
                }
            },
            _ => {
                error!("Other mirrorings not supported");
                panic!("Other mirrorings not supported");
            }
        }
    }

    fn write_to_internal_memory(&mut self, address: usize, value: u8) {
        let mirrored_address = address & (NAMETABLE_MIRROR_MASK as usize);
        let name_table_index = mirrored_address / PPU_MEMORY_SIZE;
        let mirroring = self.cartridge.borrow_mut().mirroring;
        
        match mirroring {
            Mirroring::Horizontal => {
                match mirrored_address {
                    0x000..=0x3FF | 0x400..=0x7FF => {
                        self.memory[mirrored_address & (PPU_MEMORY_SIZE - 1)] = value;
                    },
                    0x800..=0xBff | 0xC00..=0xFFF => {
                        self.memory[(mirrored_address & (PPU_MEMORY_SIZE - 1))] = value;
                    },
                    _ => {
                        error!(
                            "Attempt to write to wrong mirrored address: {:X}; {:X}; {:X}; {:?}",
                            address, mirrored_address, value, mirroring
                        );
                        panic!(
                            "Attempt to write to wrong mirrored address: {:X}; {:X}; {:X}; {:?}",
                            address, mirrored_address, value, mirroring
                        );
                    }
                }
            },
            Mirroring::Vertical => {
                match mirrored_address {
                    0x000..=0x3FF | 0x800..=0xBff  => {
                        self.memory[mirrored_address & (PPU_MEMORY_SIZE - 1)] = value;
                    },
                    0x400..=0x7FF | 0xC00..=0xFFF => {
                        self.memory[PPU_MEMORY_SIZE + (mirrored_address & (PPU_MEMORY_SIZE - 1))] = value;
                    },
                    _ => {
                        error!(
                            "Attempt to write to wrong mirrored address: {:X}; {:X}; {:X}; {:?}",
                            address, mirrored_address, value, mirroring
                        );
                        panic!(
                            "Attempt to write to wrong mirrored address: {:X}; {:X}; {:X}; {:?}",
                            address, mirrored_address, value, mirroring
                        );
                    }
                }
            },
            _ => {
                error!("Other mirrorings not supported");
                panic!("Other mirrorings not supported");
            }
        }
    }

    pub fn read_u8(&mut self, address: u16) -> u8 {
        // let address = self.address_register.get();
        let mut result;

        match address {
            CHR_ROM_PAGE_START..=CHR_ROM_PAGE_END => {
                result = self.cartridge.borrow().ppu_read_u8(address as usize);
                debug!("!!!Reading from CHR rom page {:04X}; value = {:02X}", address, result);           
            },
            VRAM_PAGE_START..=VRAM_PAGE_END => {
                result = self.read_from_internal_memory(address as usize);
            },
            PALETTE_PAGE_START..=PALETTE_PAGE_END => {
                // mirror to palette 0..=31
                let mut address = (address as usize) & (PALETTE_TABLE_SIZE - 1);

                if PALETTE_INTERNAL_MIRRORS.iter().find(|x| **x == address).is_some() {
                    address -= 0x10;
                }
                
                result = self.palette[address];
            },
            _ => {
                error!("Attempt to read from unexpected address {:X}", address);
                panic!("Attempt to read from unexpected address {:X}", address);
            }
        }

        return result;
    }

    pub fn write_u8(&mut self, address: u16, value: u8) {
        match address {
            CHR_ROM_PAGE_START..=CHR_ROM_PAGE_END => {
                self.cartridge.borrow_mut().ppu_write_u8(address as usize, value);
                debug!("!!!Writing to CHR rom page {:04X}; value = {:02X}", address, value);           
            },
            VRAM_PAGE_START..=VRAM_PAGE_END => {
                self.write_to_internal_memory(address as usize, value);
            },
            PALETTE_PAGE_START..=PALETTE_PAGE_END => {
                // mirror to palette 0..=31
                let mut address = (address as usize) & (PALETTE_TABLE_SIZE - 1);

                if PALETTE_INTERNAL_MIRRORS.iter().find(|x| **x == address).is_some() {
                    address -= 0x10;
                }
                
                self.palette[address] = value;
            },
            _ => {
                error!("Attempt to read from unexpected address {:X}", address);
                panic!("Attempt to read from unexpected address {:X}", address);
            }
        }
        // self.increment_address_register();
    }

    fn is_end_of_frame(&self) -> bool {
        return self.scanlines == SCANLINES_PER_FRAME && self.cycles == 1;
    }

    fn new_frame_reset(&mut self) {
        self.status_register.reset();
        // shifters
    }

    fn update_sprite_shifters(&mut self) {
        if self.mask_register.is_background_enabled() {
            self.background_shifter_pattern_low = self.background_shifter_pattern_low.wrapping_shl(1);
            self.background_shifter_pattern_high = self.background_shifter_pattern_high.wrapping_shl(1);

            self.background_shifter_attribute_low = self.background_shifter_attribute_low.wrapping_shl(1);
            self.background_shifter_attribute_high = self.background_shifter_attribute_high.wrapping_shl(1);
        }
    }

    fn increment_scroll_x(&mut self) {
        if self.mask_register.is_render_enabled() {
            self.address_register.increment_coarse_x();
        }
    }

    fn increment_scroll_y(&mut self) {
        if self.mask_register.is_render_enabled() {
            self.address_register.increment_coarse_y();
        }
    }

    fn transfer_x_address(&mut self) {
        if self.mask_register.is_render_enabled() {
            self.address_register.transfer_x_from(&self.temp_address_register);
        }
    }

    fn transfer_y_address(&mut self) {
        if self.mask_register.is_render_enabled() {
            self.address_register.transfer_y_from(&self.temp_address_register);
        }
    }

    fn check_nmi_interrupt(&mut self) {
        if self.scanlines >= SCANLINES_PER_FRAME && self.scanlines < SCANLINES_COUNT {
            if  self.is_end_of_frame() {
                self.status_register.insert(Status::VERTICAL_BLANK);

                if self.control_register.contains(Controller::GENERATE_NMI) {
                    warn!("Generating NMI");
                    self.nmi_interrupt = true;
                }
            }
        }
    }

    fn get_background_pixel_info(&self) -> (u8, u8) {
        if self.mask_register.is_background_enabled() {
            if self.mask_register.contains(Mask::LEFTMOST_SHOW_BACKGROUND) && self.cycles > 8 {
                let mux = 0x8000u16 >> (self.fine_x as u16);
                
                let plane_pixel_0 = ((self.background_shifter_pattern_low & mux) > 0) as u8;
                let plane_pixel_1 = ((self.background_shifter_pattern_high & mux) > 0) as u8;

                let background_pixel = (plane_pixel_1 << 1) | plane_pixel_0;

                let pixel_palette_0 = ((self.background_shifter_attribute_low & mux) > 0) as u8;
                let pixel_palette_1 = ((self.background_shifter_attribute_high & mux) > 0) as u8;
                
                let background_pixel_palette = (pixel_palette_1 << 1) | pixel_palette_0;

                return (background_pixel, background_pixel_palette);
            }
        }

        return (0, 0);
    }

    fn load_background_shifters(&mut self) {
        self.background_shifter_pattern_low = (self.background_shifter_pattern_low & 0xFF00) | self.next_background_tile_lsb as u16;
        self.background_shifter_pattern_high = (self.background_shifter_pattern_high & 0xFF00) | self.next_background_tile_msb as u16;
        
        self.background_shifter_attribute_low =
            (self.background_shifter_attribute_low & 0xFF00) | if self.next_background_tile_attribute & 0b01 > 0 {
                0xFF
            } else {
                0x00
            };

        self.background_shifter_attribute_high = 
            (self.background_shifter_attribute_high & 0xFF00) |if self.next_background_tile_attribute & 0b10 > 0 {
                0xFF
            } else {
                0x00
            };
    }
    
    fn load_background_info(&mut self) {
        match (self.cycles - 1) % 8 {
            0 => {
                self.load_background_shifters();
                self.next_background_tile_id = self.read_from_internal_memory(
                    self.address_register.vram_address() as usize
                );
            },
            2 => {
                let address = ATTRIBUTE_MEMORY_OFFSET | self.address_register.next_tile_attribute_address();
                self.next_background_tile_attribute = self.read_from_internal_memory(address as usize);
                
                if (self.address_register.coarse_y() & 0x2) != 0 {
                    self.next_background_tile_attribute >>= 4;
                }
                
                if (self.address_register.coarse_x() & 0x2) != 0 {
                    self.next_background_tile_attribute >>= 2;
                }
            },
            4 => {
                let mut address: u16;
                
                if self.control_register.contains(Controller::BACKROUND_PATTERN_ADDRESS) {
                    address = 1 << 12;
                } else {
                    address = 0;
                }

                address += (self.next_background_tile_id as u16) << 4;
                address += self.address_register.fine_y() as u16;

                self.next_background_tile_lsb = self.read_u8(address);                                  
            },
            6 => {
                let mut address: u16;
                
                if self.control_register.contains(Controller::BACKROUND_PATTERN_ADDRESS) {
                    address = 1 << 12;
                } else {
                    address = 0;
                }

                address += (self.next_background_tile_id as u16) << 4;
                address += self.address_register.fine_y() as u16;
                address += 8;

                self.next_background_tile_msb = self.read_u8(address);  
            },
            7 => {
                self.increment_scroll_x();
            },
            _ => {},
        }
    }

    pub fn tick(&mut self) {
        if self.scanlines >= -1 && self.scanlines < (SCANLINES_PER_FRAME - 1) {
            if self.scanlines == 0 && self.cycles == 0 && self.mask_register.is_render_enabled() {
                self.cycles = 1;
            }

            if self.scanlines == -1 && self.cycles == 1 {
                debug!("Resetting frame");
                self.new_frame_reset()
            }
            
            if (self.cycles >= 2 && self.cycles <= 257) || (self.cycles >= 321 && self.cycles <= 337) {
                debug!("Updating sprite shifters");
                self.update_sprite_shifters();
                
                self.load_background_info();
            }

            if self.cycles == VISIBLE_SCANLINE_CYCLES {
                self.increment_scroll_y();
            }
            
            if self.cycles == VISIBLE_SCANLINE_CYCLES + 1 {
                self.load_background_shifters();
                self.transfer_x_address();
            }

            if self.cycles == 338 || self.cycles == 340 {
                self.next_background_tile_id = self.read_from_internal_memory(
                    self.address_register.vram_address() as usize
                );
            }

            if self.scanlines == -1 && self.cycles >= 280 && self.cycles < 305 {
                self.transfer_y_address();
            } 
        }

        self.check_nmi_interrupt();

        let (background_pixel, background_pixel_palette) = self.get_background_pixel_info();
        
        if self.scanlines >= 0 && (self.scanlines as usize) < SCREEN_HEIGHT {
            if self.cycles > 0 && self.cycles <= SCREEN_WIDTH {
                self.draw_pixel(
                    (self.cycles - 1) as usize, self.scanlines as usize,
                    background_pixel, background_pixel_palette
                );
            }
        }

        self.cycles += 1;
        self.total_cycles = self.total_cycles.wrapping_add(1);

        self.notify_cartridge();
        self.increment_scanline();
    }

    fn notify_cartridge(&mut self) {
        if self.mask_register.is_render_enabled() {
            self.cartridge.borrow_mut().mapper.scanline();
        }
    }
    fn increment_scanline(&mut self) {
        if self.cycles >= CYCLES_TO_DRAW_SCANLINE {
            self.cycles = 0;
            self.scanlines += 1;

            if self.scanlines >= SCANLINES_COUNT {
                self.scanlines = -1;
                self.completed_frame = true;
                self.odd_frame = !self.odd_frame;
            }
        }
    }

    pub fn draw_pixel(&mut self, x: usize, y: usize, pixel: u8, palette: u8) {
        let palette_address = self.read_u8(
            PALETTE_MEMORY_START + (palette << 2) as u16 + pixel as u16
        );
        let color = palette_address;
        self.screen[y][x] = color;   
    }
}