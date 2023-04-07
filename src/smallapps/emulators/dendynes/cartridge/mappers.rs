use super::Header;

pub enum MapperType {
    NROM = 0,
}

pub trait Mapper {
    fn map_cpu_read(&self, index: usize) -> usize;
    
    fn map_cpu_write(&mut self, index: usize, value: u8) -> usize {
        return index;
    }

    fn map_ppu_read(&self, index: usize) -> usize;
    
    fn map_ppu_write(&mut self, index: usize, value: u8) -> usize {
        return index;
    }
}

mod nrom_mapper {
    use crate::smallapps::emulators::dendynes::cartridge::Header;

    pub const FIRST_PAGE_START: usize = 0x8000;
    pub const BANK_PAGE_SIZE: usize = 0x4000;

    pub struct NROMMapper {
        pub prg_banks_count: u8,
    }
    
    impl NROMMapper {
        pub fn new(settings: Header) -> Self {
            let mut mapper = NROMMapper {
                prg_banks_count: settings.prg_banks_count,
            };
    
            return mapper;
        }
    }
}

impl Mapper for nrom_mapper::NROMMapper {
    fn map_cpu_read(&self, index: usize) -> usize {
        if self.prg_banks_count > 1 {
            let memory_span = nrom_mapper::BANK_PAGE_SIZE * self.prg_banks_count as usize;
            
            return index & (memory_span & 1); 
        } else {
            return index & (nrom_mapper::BANK_PAGE_SIZE - 1);
        }
    }

    fn map_ppu_read(&self, index: usize) -> usize {
        return index;
    }
}

pub fn new_mapper_by_type(mapper_type: MapperType, settings: Header) -> impl Mapper {
    return match mapper_type {
        MapperType::NROM => nrom_mapper::NROMMapper::new(settings),
    };
}