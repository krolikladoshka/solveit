// https://leetcode.com/problems/making-a-large-island/
use std::collections::{HashMap, HashSet, VecDeque};

pub struct Solution;

const DIRECTIONS: [(i32, i32); 4] = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1),
];

type Point = (usize, usize);

impl Solution {
    fn get_neighbor(grid: &Vec<Vec<i32>>, ti: i32, tj: i32) -> Option<i32> {
        let n = grid.len() as i32;

        if ti >= 0 && ti < n as i32 && tj >= 0 && tj < n as i32 {
            Some(grid[ti as usize][tj as usize])
        } else {
            None
        }
    }

    fn bfs(grid: &mut Vec<Vec<i32>>, point: Point, island_number: usize, visited: &mut HashSet<Point>) -> usize {
        let n = grid.len();
        let mut queue: VecDeque<(Point, usize)> = VecDeque::with_capacity(n);
        queue.push_back((point, 1));
        visited.insert(point);
        
        let mut island_size = 0;

        while let Some(((land_i, land_j), size)) = queue.pop_front() {
            grid[land_i][land_j] = island_number as i32;
            island_size += 1;

            for direction in DIRECTIONS {
                let ti = land_i as i32 + direction.0;
                let tj = land_j as i32 + direction.1;

                if let Some(cell_value) = Self::get_neighbor(grid, ti, tj) {
                    let next_point = (ti as usize, tj as usize);

                    if visited.contains(&next_point) || cell_value != 1 {
                        continue;
                    }
                    
                    visited.insert(next_point);
                    queue.push_back((next_point, size + 1));
                }
            }
        }

        return island_size;
    }

    pub fn largest_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut island_sizes: HashMap<usize, usize> = HashMap::new();
        let mut visited: HashSet<Point> = HashSet::with_capacity(n * n);
        let mut island_number = 1;

        for i in 0..n {
            for j in 0..n {
                if !visited.contains(&(i, j)) {
                    if grid[i][j] != 0 {
                        let island_size = Self::bfs(
                            &mut grid, (i, j), island_number, &mut visited
                        );

                        island_sizes.insert(island_number, island_size);
                        island_number += 1;
                    }
                } 
            }
        }
        // return grid;

        if island_sizes.len() == 0 {
            return 1;
        }
        
        let mut new_maximum_area = *island_sizes.values().max().unwrap_or(&0);

        for i in 0..n {
            for j in 0..n {
                if grid[i][j] != 0 {
                    continue;
                }
                
                let mut sum_of_neighbor_islands = 1;
                let mut seen_islands: HashSet<i32> = HashSet::new();

                for direction in DIRECTIONS {
                    let ti = i as i32 + direction.0;
                    let tj = j as i32 + direction.1;

                    if let Some(neighbor) = Self::get_neighbor(&grid, ti, tj) {
                        if seen_islands.contains(&neighbor) {
                            continue;
                        }

                        if let Some(neighbor_size) = island_sizes.get(&(neighbor as usize)) {
                            sum_of_neighbor_islands += neighbor_size;
                            seen_islands.insert(neighbor);
                        }
                    }
                }
                new_maximum_area = std::cmp::max(new_maximum_area, sum_of_neighbor_islands);                
                }
            }
        
        return new_maximum_area as i32;
    }
}
