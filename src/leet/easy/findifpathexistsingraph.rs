use std::collections::{HashSet, VecDeque};
pub struct Solution;

impl Solution {
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        let mut adjacency_list = vec![vec![]; n as usize];

        for edge in &edges {
            let a = edge[0] ;
            let b = edge[1];
            
            adjacency_list[a as usize].push(b);
            adjacency_list[b as usize].push(a);
        }
        let mut seen: HashSet<i32> = HashSet::new();
        let mut queue: VecDeque<i32> = VecDeque::with_capacity(n as usize);
        
        queue.push_back(source);
        seen.insert(source);
 
        while let Some(node) = queue.pop_front() {
            if node == destination {
                return true;
            }

            for &neighbor in &adjacency_list[node as usize] {
                if !seen.contains(&neighbor) {
                    seen.insert(neighbor);
                    queue.push_back(neighbor);
                }
            }
        }
        
        return false;
    }
}
