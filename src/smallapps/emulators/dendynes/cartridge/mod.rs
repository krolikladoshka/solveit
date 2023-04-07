pub mod mappers;

use core::{panic};

use bitflags::bitflags;
use log::{debug, info, error};
use nom::{bytes::streaming::take, IResult, number::complete::be_u8, error::{ErrorKind, make_error}};

use self::mappers::{Mapper, MapperType, new_mapper_by_type};


impl From<u8> for MapperType {
    fn from(value: u8) -> Self {
        return match value {
            0 => MapperType::NROM,
            _ => panic!("Unable to convert {} to MapperType", value),
        };
    }
}

impl Into<u8> for MapperType {
    fn into(self) -> u8 {
        return match self {
            MapperType::NROM => 0,
        };
    }
}

const HEADER_NAME_SIZE: usize = 4;
const HEADER_UNUSED_PADDING: usize = 4;

const PRG_BANK_SIZE: usize = 0x4000;
const CHR_BANK_SIZE: usize = 0x2000;
const DETECT_NES2_FORMAT_MASK: u8 = 0b1100;

const BIT_FLAGS_MASK: u8 = 0b1111;
const TRAINER_SIZE: usize = 512;


bitflags! {
    #[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
    pub struct CartridgeMapperFlags: u8 {
        const MIRRORING   = 0b0001;
        const BATTERY     = 0b0010;
        const TRAINER     = 0b0100;
        const FOUR_SCREEN = 0b1000;
    }
}

#[derive(Debug, Clone, Copy)]
pub struct Header {
    pub name: [u8; HEADER_NAME_SIZE],
    pub prg_banks_count: u8,
    pub chr_banks_count: u8,
    pub mapper_flags: CartridgeMapperFlags,
    pub prg_ram_size: u8,
    pub mapper_id: u8,
}

// impl Clone for Header {
//     fn clone(&self) -> Self {
//         return Header {
//             name: self.name.clone(),
//             prg_banks_count: self.prg_banks_count.clone(),
//             chr_banks_count: self.chr_banks_count.clone(),
//             mapper_flags: CartridgeMapperFlags::from_bits(self.mapper_flags.bits().clone()).unwrap(),
//             prg_ram_size: self.prg_ram_size.clone(),
//             mapper_id: self.mapper_id.clone(),
//         };
//     }

//     fn clone_from(&mut self, source: &Self) {
//         self.name = source.name.clone();
//         self.prg_banks_count = source.prg_banks_count.clone();
//         self.chr_banks_count = source.chr_banks_count.clone();
//         self.mapper_flags = CartridgeMapperFlags::from_bits(source.mapper_flags.bits().clone()).unwrap();
//         self.prg_ram_size = source.prg_ram_size.clone();
//         self.mapper_id = source.mapper_id.clone();
//     }
// }

// impl Copy for Header {}


pub struct Cartridge {
    pub header: Header,

    pub prg_memory: Vec<u8>,
    pub chr_memory: Vec<u8>,
    
    pub mapper_type: MapperType,
    
    pub prg_banks_count: u8,
    pub chr_banks_count: u8,
    pub mapper: Box<dyn Mapper>,
}

impl Cartridge {
    fn load_rom_data(rom_dump_path: &str) -> Vec<u8> {
        match std::fs::read(rom_dump_path) {
            Ok(data) => {
                return data;
            },
            Err(error) => {
                panic!("Could not load rom from {}; Error: {}", rom_dump_path, error);
            }
        }
    }

    fn read_header(data: &[u8]) -> IResult<&[u8], Header> {
        let (data, name) = take(HEADER_NAME_SIZE as u8)(data)?;
        
        debug!("Cartridge TAG {:?}", name);
        
        let (data, prg_banks_count) = be_u8(data)?;
        let (data, chr_banks_count) = be_u8(data)?;
        let (data, mapper_flags_byte) = be_u8(data)?;

        let cartridge_mapper_flags = CartridgeMapperFlags::from_bits(
            mapper_flags_byte & BIT_FLAGS_MASK
        ).unwrap();

        let (data, mapper_flags_2_byte) = be_u8(data)?;

        if (mapper_flags_2_byte & DETECT_NES2_FORMAT_MASK) >> 2 == 2 {
            return Err(nom::Err::Failure(
                make_error(data, ErrorKind::NoneOf)
            ));
        }
        
        let mapper = (mapper_flags_byte & 0b11110000) | (mapper_flags_2_byte >> 4); 
        debug!("Cartridge mapper {}", mapper);
        
        let (data, prg_ram_size) = be_u8(data)?;
        let (data, test) = be_u8(data)?;

        let (mut data, _) = take(2 + HEADER_UNUSED_PADDING)(data)?;
        
        if cartridge_mapper_flags.contains(CartridgeMapperFlags::TRAINER) {
            let (_data, _) = take(TRAINER_SIZE)(data)?;
            data = _data;
        }

        let header = Header {
            name: name.try_into().unwrap(),
            prg_banks_count: prg_banks_count,
            chr_banks_count: chr_banks_count,
            mapper_flags: cartridge_mapper_flags,
            prg_ram_size: prg_ram_size,
            mapper_id: mapper,
        };
        info!("Parsed cartridge header {:?}", header);

        return Ok((data, header));

    }
    
    fn read_rom_data<'a, 'b>(data: &'a [u8], header: &'b Header) -> IResult<&'a [u8], (Vec<u8>, Vec<u8>)> {
        let (data, prg_rom) = take((header.prg_banks_count as usize) * PRG_BANK_SIZE)(data)?;
        let (data, chr_rom) = take((header.chr_banks_count as usize) * CHR_BANK_SIZE)(data)?;
        
        return Ok((data, (prg_rom.to_vec(), chr_rom.to_vec())));
    }

    pub fn new(rom_dump_path: &str) -> Self {
        let data = Self::load_rom_data(rom_dump_path);
        
        let (data, header) = match Self::read_header(data.as_slice()) {
            Ok((data, header)) => (data, header),
            Err(err) => {
                error!("Could not load ROM file: failed to parse header; {}", err);
                panic!("Could not load ROM file: failed to parse header; {}", err)
            },
        };
        
        let (prg_rom, chr_rom) = match Self::read_rom_data(data, &header) {
            Ok((_, result)) => result,
            Err(err) => panic!("Could not load ROM file: failed to parse PRG & CHR roms; {}", err),
        };
        let mapper = Box::new(
            new_mapper_by_type(
                header.mapper_id.into(),
                header.clone(),
            )
        );

        let rom = Cartridge {
            header: header,
            prg_memory: prg_rom,
            chr_memory: chr_rom,
            mapper_type: header.mapper_id.into(),
            prg_banks_count: header.prg_banks_count,
            chr_banks_count: header.chr_banks_count,
            mapper: mapper,
        };

        return rom;
    }

    pub fn cpu_read_u8(&self, index: usize) -> u8 {
        let mapped_index = self.mapper.map_cpu_read(index);
        debug!("Reading from cartridge rom: PC {:X}; Mapped PC {:X}", index, mapped_index);

        return self.prg_memory[mapped_index];
    }

    pub fn cpu_write_u8(&mut self, index: usize, value: u8) {
        let mapped_index = self.mapper.map_cpu_write(index, value);

        self.prg_memory[mapped_index] = value;
    }
    
    pub fn ppu_read_u8(&self, index: usize) -> u8 {
        let mapped_index = self.mapper.map_ppu_read(index);

        return self.chr_memory[mapped_index];
    }

    pub fn ppu_write_u8(&mut self, index: usize, value: u8) {
        let mapped_index = self.mapper.map_ppu_write(index, value);

        self.chr_memory[mapped_index] = value;
    }
}
