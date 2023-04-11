use core::borrow;
use std::{path::Path, rc::Rc, cell::RefCell, borrow::{BorrowMut, Borrow}, time::SystemTime};
use graphics::{image, Transformed};
use ::image::{ImageBuffer, RgbImage, RgbaImage};
use log::warn;
use piston::{WindowSettings, Event, Loop};
use piston_window::{PistonWindow, Texture, TextureSettings};
use crate::smallapps::emulators::dendynes::{logging::init_logger, ppu::{CYCLES_TO_DRAW_SCANLINE, SCANLINES_PER_FRAME, SCANLINES_COUNT, SCREEN_WIDTH, SCREEN_HEIGHT, PALETTE}};

use self::{bus::Bus, cartridge::Cartridge, ppu::PPU, cpu::processor::CPU};

pub mod bus;
pub mod cpu;
pub mod memory;
pub mod cartridge;
pub mod logging;
pub mod ppu;


pub struct Dendy {
}
const WINDOW_WIDTH: usize = 800;
const WINDOW_HEIGHT: usize = 600;

fn clock_cpu(cpu: &mut CPU, cycles_to_run: usize) {
    let mut cycles = 0;
    
    while cycles < cycles_to_run {
        let elapsed_cpu_cycles = cpu.cpu_step();

        cycles += elapsed_cpu_cycles.round() as usize;
    }
}

pub fn dendy_run() {
    init_logger().unwrap();
    
    warn!("Started app");

    let current_file = Path::new(file!());

    // let cartridge_path = "tests/roms/donkey kong.nes";
    let cartridge_path = "tests/roms/nestest.nes";
    let cartridge_path = current_file.parent().unwrap().join(cartridge_path);

    let mut cartridge = Rc::new(
        RefCell::new(
            Cartridge::new(cartridge_path.as_os_str().to_str().unwrap())
        )
    );
    let mut ppu_device = PPU::new(cartridge.clone());
    
    let mut bus = Bus::new(&mut ppu_device, cartridge.clone());
    let mut cpu = CPU::new(&mut bus);

    // cpu.run();

    let mut window: PistonWindow = WindowSettings::new(
        "Dendynes emulator", [WINDOW_WIDTH as f64, WINDOW_HEIGHT as f64]
    ).exit_on_esc(true)
     .build()
     .unwrap();
    let cpu_cycles_for_frame = CYCLES_TO_DRAW_SCANLINE * (SCANLINES_COUNT as usize);
    let cpu_cycles_for_frame = ((cpu_cycles_for_frame as f32) / 3f32).round() as usize;

    let mut image_buffer = RgbaImage::new(SCREEN_WIDTH as u32, SCREEN_HEIGHT as u32);
    let mut table_image_buffer_1 = RgbaImage::new(128, 128);
    let mut table_image_buffer_2 = RgbaImage::new(128, 128);

    let mut texture_context = &mut window.create_texture_context();

    let mut texture = Texture::from_image(
        texture_context, &image_buffer, &TextureSettings::new()
    ).unwrap();

    let mut table_texture_1 = Texture::from_image(
        texture_context, &table_image_buffer_1, &TextureSettings::new()
    ).unwrap();
    let mut table_texture_2 = Texture::from_image(
        texture_context, &table_image_buffer_2, &TextureSettings::new()
    ).unwrap();


    while let Some(event) = window.next() {
        match event {
            Event::Input(input, _) => {
            },
            Event::Loop(kind) => {
                match kind {
                    Loop::Update(args) => {
                        let cycles_per_update = ((cpu_cycles_for_frame as f64) * args.dt).round() as usize;

                        let start = SystemTime::now();
                        clock_cpu(cpu.borrow_mut(), cycles_per_update);
                        let end = SystemTime::now();

                        println!(
                            "Update took: dt {}; clock: {}ms; {}s",
                            args.dt,
                            end.duration_since(start).unwrap().as_millis(),
                            end.duration_since(start).unwrap().as_secs_f32(),
                        );
                    },
                    Loop::Render(_args) => {
                        window.draw_2d(&event, |c, g, d| {
                            let start = SystemTime::now();
                            let screen = &cpu.borrow().bus.ppu.screen;
                            for y in 0..SCREEN_HEIGHT {
                                for x in 0..SCREEN_WIDTH {
                                    let nes_color = screen[y][x];
                                    let pixel = PALETTE[nes_color as usize];
                                    image_buffer.put_pixel(x as u32, y as u32, ::image::Rgba(
                                        [pixel[0], pixel[1], pixel[2], 255],
                                    )
                                    );
                                }
                            }                     
                            let end1 = SystemTime::now();

                            {
                                cpu.borrow_mut().bus.ppu.draw_pattern_tables();
                            }
                            for y in 0..128 {
                                for x in 0..128 {
                                    let nes_color = cpu.borrow().bus.ppu.debug_pattern_tables[0][y][x];
                                    let pixel = PALETTE[nes_color as usize];
                                    table_image_buffer_1.put_pixel(x as u32, y as u32, ::image::Rgba(
                                        [pixel[0], pixel[1], pixel[2], 255],
                                    )
                                    );
                                }
                            } 
                            for y in 0..128 {
                                for x in 0..128 {
                                    let nes_color = cpu.borrow().bus.ppu.debug_pattern_tables[1][y][x];
                                    let pixel = PALETTE[nes_color as usize];
                                    table_image_buffer_2.put_pixel(x as u32, y as u32, ::image::Rgba(
                                        [pixel[0], pixel[1], pixel[2], 255],
                                    )
                                    );
                                }
                            }               

                            // println!("######### RENDER");
                            // println!("{:?}", cpu.borrow().bus.ppu.screen);

                            texture.update(texture_context, &image_buffer).unwrap();
                            table_texture_1.update(texture_context, &table_image_buffer_1).unwrap();
                            table_texture_2.update(texture_context, &table_image_buffer_1).unwrap();
                            
                            image(&texture, c.transform.scale(2f64, 2f64), g);
                            image(&table_texture_1, c.transform.trans((SCREEN_WIDTH * 2) as f64, 0f64), g);
                            image(&table_texture_2, c.transform.trans((SCREEN_WIDTH * 3) as f64, 0f64), g);
                            let end2 = SystemTime::now();

                            texture_context.encoder.flush(d);
                            let end3 = SystemTime::now();
                            println!(
                                "Draw took: {}; Texture update: {}; Flush: {}",
                                end1.duration_since(start).unwrap().as_secs_f32(),
                                end2.duration_since(start).unwrap().as_secs_f32(),
                                end3.duration_since(start).unwrap().as_secs_f32()
                            )

                            
                        });
                    },
                    _ => {},
                }
            },
            _ => {}
        }
    }
    
}