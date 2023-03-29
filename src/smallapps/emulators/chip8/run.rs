extern crate graphics;
extern crate piston;

use std::path::Path;

use graphics::types::Color;
use graphics::{clear, rectangle, Context};
use piston::{Loop, Event};
use piston::event_loop::{EventSettings, Events};
use piston::input::{RenderArgs, RenderEvent, UpdateArgs, UpdateEvent};
use piston::window::WindowSettings;
use piston_window::{PistonWindow, G2d, GfxDevice};

use super::cpu::{Chip8, self, DISPLAY_HEIGHT, DISPLAY_WIDTH};

const WINDOW_WIDTH: usize = 640;
const WINDOW_HEIGHT: usize = 320;
const BLOCK_WIDTH: usize = WINDOW_WIDTH / cpu::DISPLAY_WIDTH;
const BLOCK_HEIGHT: usize = WINDOW_HEIGHT / cpu::DISPLAY_HEIGHT;

pub struct Chip8Emulator {
    chip8: Chip8,
    window: PistonWindow,
}

impl Chip8Emulator {
    pub fn new() -> Self {
        return Chip8Emulator {
            chip8: Chip8::new(),
            window: WindowSettings::new(
                "Chip8 emulator", [WINDOW_WIDTH as f64, WINDOW_HEIGHT as f64]
            ).exit_on_esc(true)
             .build()
             .unwrap(),
        };
    }

    pub fn load_rom(&mut self, path: &str) {
        let this_path = Path::new(file!());
        let path = this_path.parent().unwrap().join(path);
        self.chip8.load_program(&path);
    }

    pub fn run(&mut self) {
        while let Some(event) = self.window.next() {
            match event {
                Event::Loop(l) => {
                    match l {
                        Loop::Update(_args) => self.chip8.cycle(),
                        Loop::Render(_args) => {
                            self.window.draw_2d(&event,
                                |context, graphics, _device| {
                                    clear([0.0; 4], graphics);
                                    
                                    for y in 0..DISPLAY_HEIGHT {
                                        for x in 0..DISPLAY_WIDTH {
                                            let mut color = [0.0f32; 4];
                                            
                                            if self.chip8.canvas[y][x] == 1 {
                                                color = [1.0f32; 4];
                                            }
                
                                            rectangle(
                                                color,
                                                [
                                                    (x * BLOCK_WIDTH) as f64, (y * BLOCK_HEIGHT) as f64,
                                                    BLOCK_WIDTH as f64, BLOCK_HEIGHT as f64
                                                ],
                                                context.transform,
                                                graphics
                                            );
                                        }
                                    }
                                }
                            );
                        }
                        _ => {}
                    }
                },
                _ => {}
            }
        }
    }
}

pub fn chip8_run() {
    let mut emulator = Chip8Emulator::new();
    // emulator.load_rom("tests/IBMlogo.ch8");
    emulator.load_rom("tests/test_opcode.ch8");

    emulator.run();    
}