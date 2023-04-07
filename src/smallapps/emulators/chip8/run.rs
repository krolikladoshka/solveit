extern crate graphics;
extern crate piston;

use std::path::Path;

use graphics::{clear, rectangle};
use piston::{Loop, Event, Input, Button, Key, ButtonState};
use piston::input::{UpdateArgs};
use piston::window::WindowSettings;
use piston_window::{PistonWindow};

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
        let mut buttons = [
            (Key::D1, 1), (Key::D2, 2), (Key::D3, 3), (Key::D4, 0xC),
            (Key::Q, 4), (Key::W, 5), (Key::E, 6), (Key::R, 0xD),
            (Key::A, 7), (Key::S, 8), (Key::D, 9), (Key::F, 0xE),
            (Key::Z, 0xA), (Key::X, 0), (Key::C, 0xB), (Key::V, 0xF),
        ];
        
        let cpu_frequency = 700;
        let timer_frequency = 1f64/ 60f64;

        let mut last_time = 0f64;

        while let Some(event) = self.window.next() {
            match event {
                Event::Input(input, _) => {
                    match input {
                        Input::Button(args) => {
                            if let Button::Keyboard(key) = args.button {
                                if let Some(key_index) = buttons.iter().position(|&(k, _)| k == key) {
                                    match args.state {
                                        ButtonState::Press => self.chip8.keys[buttons[key_index].1] = 1,
                                        ButtonState::Release => self.chip8.keys[buttons[key_index].1] = 0
                                    }
                                }
                            }
                        },
                         _ => {}
                    }
                },
                Event::Loop(l) => {
                    match l {
                        Loop::Update(UpdateArgs{dt}) => {
                            println!("DT {}", dt);
                            if last_time >= timer_frequency {
                                let ticks = (last_time / timer_frequency) as u8;
                            
                                self.chip8.decrement_timers(ticks);
                            
                                last_time = last_time - timer_frequency;
                                println!("Ticks & last time {} {}", ticks, last_time);
                            }
                            println!("dt {}", dt);
                            
                            let cycles_to_run = (dt * cpu_frequency as f64).round() as usize;
                            println!("cycles to run {}", cycles_to_run);
                            for i in 0..cycles_to_run {
                                self.chip8.cycle();
                            }
                            last_time += dt;
                            println!("last time after {}", last_time);
                        },
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
    emulator.load_rom("tests/Tank.ch8");

    emulator.run();    
}