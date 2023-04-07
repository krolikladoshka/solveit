use log::{warn, debug, error};

use super::{ppu::PPU, cartridge::Cartridge, memory::accessing_mode::MemoryAccessMode};

const CPU_MEMORY_SIZE: usize = 0x800;

const CPU_RAM_PAGE_START: usize = 0;
const CPU_RAM_PAGE_END: usize = 0x1FFF;
const CPU_RAM_MIRROR_MASK: usize = 0b0111_1111_1111;

const IO_PAGE_START: usize = 0x2008;
const IO_PAGE_END: usize = 0x3FFF;
const IO_MIRROR_MASK: usize = 0b10000000000111;

const PPU_CTRL_ADDRESS: usize = 0x2000;
const PPU_MASK_ADDRESS: usize = 0x2001;
const PPU_STATUS_ADDRESS: usize = 0x2002;
const OAM_ADDRESS: usize = 0x2003;
const OAM_DATA_ADDRESS: usize = 0x2004;
const PPU_SCROLL: usize = 0x2005;
const PPU_ADDRESS: usize = 0x2006;
const PPU_DATA_ADDRESS: usize = 0x2007;
const OAM_DMA_ADDRESS: usize = 0x4014;

// APU & I/O
const SQ1_VOL_ADDRESS: usize = 0x4000;
const SQ1_SWEEP_ADDRESS: usize = 0x4001;
const SQ1_LO_ADDRESS: usize = 0x4002;
const SQ1_HI_ADDRESS: usize = 0x4003;
const SQ2_VOL_ADDRESS: usize = 0x4004;
const SQ2_SWEEP_ADDRESS: usize = 0x4005;
const SQ2_LO_ADDRESS: usize = 0x4006;
const SQ2_HI_ADDRESS: usize = 0x4007;
const TRI_LINEAR_ADDRESS: usize = 0x4008;
const APU_UNUSED_REGISTER_1_ADDRESS: usize = 0x4009;
const TRI_LO_ADDRESS: usize = 0x400A;
const TRI_HI_ADDRESS: usize = 0x400B;
const NOISE_VOL_ADDRESS: usize = 0x400C;
const APU_UNUSED_REGISTER_2_ADDRESS: usize = 0x400D;
const NOISE_LO_ADDRESS: usize = 0x400E;
const NOISE_HI_ADDRESS: usize = 0x400F;
const DMC_FREQ_ADDRESS: usize = 0x4010;
const DMC_RAW_ADDRESS: usize = 0x4011;
const DMC_START_ADDRESS: usize = 0x4012;
const DMC_LEN_ADDRESS: usize = 0x4013;
// const OAM_DMA_ADDRESS: usize = 0x4014;
const SND_CHN_ADDRESS: usize = 0x4015;

const JOYPAD_1_IO_ADDRESS: usize = 0x4016;
const JOYPAD_2_IO_ADDRESS: usize = 0x4017;

const APU_IO_UNUSED_PAGE_START: usize = 0x4018;
const APU_IO_UNUSED_PAGE_END: usize = 0x401F;

const CARTRIDGE_PAGE_START: usize = 0x4020;
const CARTRIDGE_PAGE_END: usize = 0xFFFF;

const PROGRAM_ROM_PAGE_START: usize = 0x8000;
const PROGRAM_ROM_PAGE_END: usize = 0xFFFF;

pub struct Bus<'a> {
    pub cpu_memory: [u8; CPU_MEMORY_SIZE],
    pub cpu_cycles: usize,
    pub ppu: &'a mut PPU,
    pub cartridge: &'a mut Cartridge,
}

impl<'a> Bus<'a> {
    pub fn new(ppu_device: &'a mut PPU, cartridge: &'a mut Cartridge) -> Self {
        let mut bus = Bus {
            cpu_memory: [0; CPU_MEMORY_SIZE],
            cpu_cycles: 0,
            ppu: ppu_device,
            cartridge: cartridge,
        };

        return bus;
    }

    pub fn load_rom(&mut self) {

    }

    pub fn poll_nmi_interrupt(&mut self) -> bool {
        return self.ppu.nmi_interrupt;
    }

    pub fn read_memory_u8(&self, index: usize) -> u8 {
        match index {
            CPU_RAM_PAGE_START..=CPU_RAM_PAGE_END => {
                return self.cpu_memory[index & CPU_RAM_MIRROR_MASK];
            },
            PPU_CTRL_ADDRESS |
            PPU_MASK_ADDRESS |
            OAM_ADDRESS      |
            PPU_SCROLL       |
            PPU_ADDRESS      |
            OAM_DMA_ADDRESS => {
                warn!("Attempt to read temporary read-only area of PPU registers {:X}", index);
                
                return 0;
            },
            PPU_STATUS_ADDRESS => {
                return self.ppu.read_status_register();
            },
            OAM_DATA_ADDRESS => {
                return self.ppu.read_oam_register();
            },
            PPU_DATA_ADDRESS => {
                return self.ppu.read_data_register();
            },
            IO_PAGE_START..=IO_PAGE_END => {
                return self.read_memory_u8(index & IO_MIRROR_MASK);
            },
            SQ1_VOL_ADDRESS..=SND_CHN_ADDRESS => {
                warn!("Attempt to read unimplemented APU registers {:X}", index);

                return 0;
            },
            JOYPAD_1_IO_ADDRESS | JOYPAD_2_IO_ADDRESS => {
                warn!("Attempt to read joypad registers {:X}", index);

                return 0;
            },
            APU_IO_UNUSED_PAGE_START..=APU_IO_UNUSED_PAGE_END => {
                warn!("Attempt to read unused APU/IO memory {:X}", index);

                return 0;
            },
            // for now
            PROGRAM_ROM_PAGE_START..=PROGRAM_ROM_PAGE_END => {
                debug!("Attempt to read program rom space {:X}", index);
                
                return self.cartridge.cpu_read_u8(index);
            },
            CARTRIDGE_PAGE_START..=CARTRIDGE_PAGE_END => {
                warn!("Attempt to read unused cartridge (PRG ROM/RAM) space {:X}", index);

                return self.cartridge.cpu_read_u8(index);
            },
            _ => {
                panic!("Failed attempt to grab memory from {}", index);
            }
        }
    }

    pub fn read_memory_u16(&self, index: usize) -> u16 {
        return u16::from_le_bytes([
            self.read_memory_u8(index), 
            self.read_memory_u8(index + 1)
        ]);
    }

    pub fn write_memory_u8(&mut self, index: usize, value: u8) {
        match index {
            CPU_RAM_PAGE_START..=CPU_RAM_PAGE_END => {
                self.cpu_memory[index & CPU_RAM_MIRROR_MASK] = value;
            },
            PPU_CTRL_ADDRESS |
            PPU_MASK_ADDRESS |
            OAM_ADDRESS      |
            PPU_SCROLL       |
            PPU_ADDRESS      |
            OAM_DMA_ADDRESS => {
                warn!("Attempt to read temporary read-only area of PPU registers {:X}", index);
                
                // return 0;
            },
            PPU_STATUS_ADDRESS => {
                // return self.ppu.read_status_register();
            },
            OAM_DATA_ADDRESS => {
                // return self.ppu.read_oam_register();
            },
            PPU_DATA_ADDRESS => {
                // return self.ppu.read_data_register();
            },
            IO_PAGE_START..=IO_PAGE_END => {
                // return self.read_memory_u8(index & IO_MIRROR_MASK);
            },
            SQ1_VOL_ADDRESS..=SND_CHN_ADDRESS => {
                warn!("Attempt to read unimplemented APU registers {:X}", index);

                // return 0;
            },
            JOYPAD_1_IO_ADDRESS | JOYPAD_2_IO_ADDRESS => {
                warn!("Attempt to read joypad registers {:X}", index);

                // return 0;
            },
            APU_IO_UNUSED_PAGE_START..=APU_IO_UNUSED_PAGE_END => {
                warn!("Attempt to write to unused APU/IO memory {:X}; value={:X}", index, value);

                // return 0;
            },
            CARTRIDGE_PAGE_START..=CARTRIDGE_PAGE_END => {
                warn!("Attempt to write to unused cartridge (PRG ROM/RAM) space {:X}; value={:X}", index, value);

                // return 0
            },
            _ => {
                error!("Failed attempt to write memory to {:X}; value={:X}", index, value);
                panic!("Failed attempt to write memory to {:X}; value={:X}", index, value);
            }
        }
    }
    
    pub fn write_memory_u16(&mut self, index: usize, value: u16) {
        let [low, high] = u16::to_le_bytes(value);

        self.write_memory_u8(index, low);
        self.write_memory_u8(index + 1, high);
    }

    pub fn tick(&mut self, cycles: f32) {
        self.cpu_cycles += cycles as usize;
        // thrice the speed of cpu
        self.ppu.tick((cycles * 3f32).round() as usize);
        // two times slower than cpu
        // self.apu.tick(cycles);
    }

}