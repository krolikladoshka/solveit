use log::warn;

pub const CYCLES_TO_DRAW_FRAME: usize = 341;

pub struct PPU {
    pub cycles: usize,
    pub nmi_interrupt: bool,
}

impl PPU {
    pub fn new() -> Self {
        let mut ppu = PPU {
            cycles: 0,
            nmi_interrupt: false,
        };

        return ppu;
    }

    pub fn read_status_register(&self) -> u8 {
        warn!("Reading unimplemented PPU status register");

        return 0;
    }

    pub fn read_oam_register(&self) -> u8 {
        warn!("Reading unimplemented PPU oam data register");

        return 0;
    }

    pub fn read_data_register(&self) -> u8 {
        warn!("Reading unimplemented PPU data register");

        return 0;
    }

    pub fn tick(&mut self, cycles: usize) {

    }
}