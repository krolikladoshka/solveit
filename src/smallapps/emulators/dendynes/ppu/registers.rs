use bitflags::bitflags;


pub const OPEN_BUS_REGISTER_MASK: u8 = (1 << 5) - 1;
pub const VRAM_ADDRESS_INC: u16 = 1;
pub const VRAM_ADDRESS_INC_VERTICAL_MODE: u16 = 32;
pub const PPU_ADDRESS_MIRROR_MASK: u16 = 0x3FFF;


bitflags! {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
    pub struct Controller: u8 {
        const NAMETABLE1                = 0b00000001;
        const NAMETABLE2                = 0b00000010;
        const VRAM_ADDRESS_INCREMENT    = 0b00000100;
        const SPRITE_PATTERN_ADDRESS    = 0b00001000;
        const BACKROUND_PATTERN_ADDRESS = 0b00010000;
        const SPRITE_SIZE               = 0b00100000;
        const MASTER_SLAVE_SELECT       = 0b01000000;
        const GENERATE_NMI              = 0b10000000;
    }

    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
    pub struct Mask: u8 {
        const GREYSCALE                = 0b0000_0001;
        const LEFTMOST_SHOW_BACKGROUND = 0b0000_0010;
        const LEFTMOST_SHOW_SPRITES    = 0b0000_0100;
        const SHOW_BACKGROUND          = 0b0000_1000;
        const SHOW_SPRITES             = 0b0001_0000;
        const EMPHASIZE_RED            = 0b0010_0000;
        const EMPHASIZE_GREEN          = 0b0100_0000;
        const EMPHASIZE_BLUE           = 0b1000_0000;
    }

    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
    pub struct Status: u8 {
        const OPENBUS0        = 0b0000_0001;
        const OPENBUS1        = 0b0000_0010;
        const OPENBUS2        = 0b0000_0100;
        const OPENBUS3        = 0b0000_1000;
        const OPENBUS4        = 0b0001_0000;
        const SPRITE_OVERFLOW = 0b0010_0000;
        const SPRITE_ZERO_HIT = 0b0100_0000;
        const VERTICAL_BLANK  = 0b1000_0000;
    }
}

impl Status {
    pub fn read(&mut self, open_bus: u8) -> u8 {
        let result = self.bits() | (open_bus & OPEN_BUS_REGISTER_MASK);
        
        self.remove(Self::VERTICAL_BLANK);

        return result;
    }
}

pub struct PPUAddress {
    pub low: u8, 
    pub high: u8,
}

pub struct Scroll {
    pub x: u8,
    pub y: u8,
}

impl PPUAddress {
    pub fn new() -> Self {
        return PPUAddress { low: 0, high: 0 };
    }

    pub fn set(&mut self, value: u16) {
        [self.low, self.high] = u16::to_le_bytes(value);
    }

    pub fn get(&self) -> u16 { 
        return u16::from_le_bytes([
            self.low,
            self.high,
        ]);
    }

    pub fn write(&mut self, byte: u8, latch: bool) {
        if !latch {
            self.high = byte;
        } else {
            self.low = byte;
        }
    }

    pub fn increment(&mut self, vertical_mode: bool) {
        let mut value = self.get();

        if vertical_mode {
            value += VRAM_ADDRESS_INC_VERTICAL_MODE;
        } else {
            value += VRAM_ADDRESS_INC;
        }

        value &= PPU_ADDRESS_MIRROR_MASK;

        self.set(value);
    }
}

impl Scroll {
    pub fn new() -> Self {
        return Scroll { x: 0, y: 0 };
    }

    pub fn write(&mut self, byte: u8, latch: bool) {
        if !latch {
            self.x = byte;
        } else {
            self.y = byte;
        }
    }
}