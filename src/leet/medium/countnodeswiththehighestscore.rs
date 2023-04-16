// https://leetcode.com/problems/count-nodes-with-the-highest-score

use std::collections::HashMap;

pub struct Solution;

impl Solution {
    fn dfs(n: u32, node: i32, graph: &HashMap<i32, Vec<usize>>, scores: &mut HashMap<u64, i32>) -> u32 {
        let mut score = 1u64;
        let mut size = 0;

        for child in graph.get(&node).unwrap_or(&vec![]) {
            let subsize = Self::dfs(n, *child as i32, graph, scores);
            score *= subsize as u64;
            size += subsize;
        }
        
        score *= std::cmp::max(1, n as u64 - 1 - size as u64);
        
        if let Some(count) = scores.get(&score) {
            scores.insert(score, count + 1);
        } else {
            scores.insert(score, 1);
        }

        return size + 1;
    }

    pub fn count_highest_score_nodes(parents: Vec<i32>) -> i32 {
        let mut graph = HashMap::new();
        let mut scores = HashMap::new();

        for (node, parent) in parents.iter().enumerate() {
            graph.entry(*parent)
                 .or_insert(vec![])
                 .push(node);
        }

        Self::dfs(parents.len() as u32, 0, &graph, &mut scores);
        
        let mut max_score = 0;

        for (score, _) in &scores {
            if *score > max_score {
                max_score = *score;
            }
        }

        return *scores.get(&max_score).unwrap();
    }
}