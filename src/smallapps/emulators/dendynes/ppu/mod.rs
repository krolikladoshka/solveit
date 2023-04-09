pub mod registers;

use std::{cell::RefCell, rc::Rc};

use log::{warn, error};

use self::registers::{Controller, Mask, Status, Scroll, PPUAddress};

use super::cartridge::{Cartridge, Mirroring};

pub const SCANLINES_COUNT: usize = 262;
pub const CYCLES_TO_DRAW_SCANLINE: usize = 341;
pub const PPU_MEMORY_SIZE: usize = 0x800;
pub const OAM_DATA_SIZE: usize = 0x100;
pub const PALETTE_TABLE_SIZE: usize = 32;

pub const PALETTE_MEMORY_START: u16 = 0x3F00;

pub const CHR_ROM_PAGE_START: u16 = 0x0000;
pub const CHR_ROM_PAGE_END: u16 = 0x1FFF;
pub const VRAM_PAGE_START: u16 = 0x2000;
pub const VRAM_PAGE_END: u16 = 0x2FFF;
pub const PALETTE_PAGE_START: u16 = 0x3F00;
pub const PALETTE_PAGE_END: u16 = 0x3FFF;
pub const PALETTE_INTERNAL_MIRRORS: [usize; 4] = [
    0x10, 0x14, 0x18, 0x1C,
];

pub const NAMETABLE_MIRROR_MASK: u16 = 0xFFF;

pub struct PPU {
    pub cycles: usize,
    pub nmi_interrupt: bool,

    pub latch: bool,
    pub control_register: Controller,
    pub mask_register: Mask,
    pub status_register: Status,
    pub oam_address_register: u8,
    pub oam_data_register: u8,
    pub scroll_register: Scroll,
    pub address_register: PPUAddress, 

    pub data_buffer: u8, 

    pub memory: [u8; PPU_MEMORY_SIZE],
    pub oam_data: [u8; OAM_DATA_SIZE],
    pub palette: [u8; PALETTE_TABLE_SIZE],

    pub cartridge: Rc<RefCell<Cartridge>>
    // pub mirroring: Mirroring,
}

impl PPU {
    pub fn new(cartridge: Rc<RefCell<Cartridge>>) -> Self {
        let mut ppu = PPU {
            cycles: 0,
            nmi_interrupt: false,
            latch: false,
            control_register: Controller::empty(),
            mask_register: Mask::empty(),
            status_register: Status::empty(),
            oam_address_register: 0,
            oam_data_register: 0,
            scroll_register: Scroll::new(),
            address_register: PPUAddress::new(),
            data_buffer: 0,
            memory: [0; PPU_MEMORY_SIZE],
            oam_data: [0; OAM_DATA_SIZE],
            palette: [0; PALETTE_TABLE_SIZE],
            cartridge: cartridge,
        };

        return ppu;
    }

    /* +register reads */
    pub fn read_status_register(&mut self) -> u8 {
        let result = self.status_register.read(self.data_buffer);
        
        self.latch = false;

        return result;
    }

    pub fn read_oam_data_register(&self) -> u8 {
        return self.oam_data[self.oam_address_register as usize];
    }

    pub fn read_data_register(&mut self) -> u8 {
        let result = self.data_buffer;
        
        if self.address_register.get() >= PALETTE_PAGE_START {
            self.data_buffer = self.read_u8();

            return self.data_buffer;
        }
        
        return result;
    }
    /* -register reads */

    /* +register writes */
    pub fn write_control_register(&mut self, value: u8) {
        self.control_register = Controller::from_bits(value).unwrap();
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
        self.scroll_register.write(value, self.latch);
        self.latch = !self.latch;
    }

    pub fn write_address_register(&mut self, value: u8) {
        self.address_register.write(value, self.latch);
        self.latch = !self.latch;
    }

    pub fn write_data_register(&mut self, value: u8) {
        self.write_u8(value);
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
        
        match self.cartridge.borrow_mut().mirroring {
            Mirroring::Horizontal => {
                match mirrored_address {
                    0x000..=0x3FF | 0x400..=0x7FF => {
                        return self.memory[mirrored_address & (PPU_MEMORY_SIZE - 1)];
                    },
                    0x800..=0xBff | 0xC00..=0xFFF => {
                        return self.memory[PPU_MEMORY_SIZE + (mirrored_address & (PPU_MEMORY_SIZE - 1))];
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
        
        match self.cartridge.borrow_mut().mirroring {
            Mirroring::Horizontal => {
                match mirrored_address {
                    0x000..=0x3FF | 0x400..=0x7FF => {
                        self.memory[mirrored_address & (PPU_MEMORY_SIZE - 1)] = value;
                    },
                    0x800..=0xBff | 0xC00..=0xFFF => {
                        self.memory[PPU_MEMORY_SIZE + (mirrored_address & (PPU_MEMORY_SIZE - 1))] = value;
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
                    } 
                }
            },
            _ => {
                error!("Other mirrorings not supported");
                panic!("Other mirrorings not supported");
            }
        }
    }

    pub fn read_u8(&mut self) -> u8 {
        let address = self.address_register.get();
        let mut result;

        match address {
            CHR_ROM_PAGE_START..=CHR_ROM_PAGE_END => {
                result = self.cartridge.borrow().ppu_read_u8(address as usize);                
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
        self.increment_address_register();

        return result;
    }

    pub fn write_u8(&mut self, value: u8) {
        let address = self.address_register.get();
        
        match address {
            CHR_ROM_PAGE_START..=CHR_ROM_PAGE_END => {
                self.cartridge.borrow_mut().ppu_write_u8(address as usize, value);                
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
        self.increment_address_register();
    }

    pub fn tick(&mut self, cycles: usize) {
        // while 
    }

    pub fn draw_pixel(&mut self) {

    }
}