// https://leetcode.com/problems/rotting-oranges/

use std::collections::{VecDeque};
pub struct Solution;

impl Solution {  
    fn rot_oranges(grid: &mut Vec<Vec<i32>>, starting_oranges: &Vec<(i32, i32)>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        
        let directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
        ];
        
        let get_neighbor = 
            |grid: &Vec<Vec<i32>>, ti: i32, tj: i32| -> Option<i32> {
                if ti >= 0 && ti < m as i32 && tj >= 0 && tj < n as i32 {
                    Some(grid[ti as usize][tj as usize])
                } else {
                    None
                }
            };

        let mut queue: VecDeque<(i32, i32, i32)> = VecDeque::with_capacity(m * n);
        for (start_i, start_j) in starting_oranges {
            queue.push_back((*start_i, *start_j, 0));
        }

        let mut elapsed = 0;
        
        while let Some((cell_i, cell_j, step_elapsed)) = queue.pop_front() {
            for (di, dj) in directions {
                let n_i = cell_i + di;
                let n_j = cell_j + dj;
                
                if let Some(neighbour) = get_neighbor(grid, n_i, n_j) {
                    if neighbour == 1 {
                        grid[n_i as usize][n_j as usize] = 2;
                        queue.push_back((n_i, n_j, step_elapsed + 1));
                    }
                }
            }
           
            elapsed = std::cmp::max(step_elapsed, elapsed);
        }

        return elapsed;
    }

    pub fn oranges_rotting(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();

        let mut elapsed = 0;
        
        let rotten_oranges:Vec<(i32, i32)> = grid
            .iter()
            .enumerate()
            .flat_map(|(i, row)| {
                row
                .iter()
                .enumerate()
                .filter(|(_, &val)| {
                    val == 2
                })
                .map(move |(j, _)| {
                    (i as i32, j as i32)
                })
            })
            .collect();

        let elapsed_local = Solution::rot_oranges(
            &mut grid, &rotten_oranges
        );
        elapsed = std::cmp::max(elapsed, elapsed_local);

        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    return -1;
                }
            }
        }

        return elapsed;   
    }
}
