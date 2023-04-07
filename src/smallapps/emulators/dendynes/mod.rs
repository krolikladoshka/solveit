use std::path::Path;
use log::warn;
use crate::smallapps::emulators::dendynes::logging::init_logger;

use self::{bus::Bus, cartridge::Cartridge, ppu::PPU, cpu::processor::CPU};

pub mod bus;
pub mod cpu;
pub mod memory;
pub mod cartridge;
pub mod logging;
pub mod ppu;


pub struct Dendy {
}


pub fn dendy_run() {
    init_logger().unwrap();
    
    warn!("Started app");

    let current_file = Path::new(file!());

    let cartridge_path = "tests/roms/nestest.nes";
    let cartridge_path = current_file.parent().unwrap().join(cartridge_path);

    let mut cartridge = Cartridge::new(cartridge_path.as_os_str().to_str().unwrap());
    let mut ppu_device = PPU::new();
    
    let mut bus = Bus::new(&mut ppu_device, &mut cartridge);
    let mut cpu = CPU::new(&mut bus);
    
    cpu.run();
}