// https://leetcode.com/problems/network-delay-time/
use std::collections::{HashMap, BinaryHeap};
use std::cmp::Ordering;

pub struct Solution;

#[derive(Clone, Copy)]
enum SignalReceived {
    Time(i32),
    Infinity
}

impl Eq for SignalReceived {}

impl PartialEq for SignalReceived {
    fn eq(&self, other: &Self) -> bool {
        self.cmp(other) == Ordering::Equal
    }
}

impl PartialOrd for SignalReceived {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for SignalReceived {
    fn cmp(&self, other: &Self) -> Ordering {
        match (self, other) {
            (SignalReceived::Infinity, SignalReceived::Infinity) => Ordering::Equal,
            (SignalReceived::Infinity, _) => Ordering::Greater,
            (_, SignalReceived::Infinity) => Ordering::Less,
            (SignalReceived::Time(t1), SignalReceived::Time(t2)) => t1.cmp(t2),
        }
    }
}

type Edge = (i32, i32);

impl Solution {
    fn calculate(graph: &HashMap<i32, Vec<Edge>>, source: i32, received_signals: &mut Vec<SignalReceived>) {

        let mut heap:BinaryHeap<Edge> = BinaryHeap::new();
        heap.push((0, source));

        while let Some((cost, node)) = heap.pop() {
            if SignalReceived::Time(cost) > received_signals[(node - 1) as usize] {
                continue;
            }

            if let Some(neighbors) = graph.get(&node) {
                for (neighbor_cost, neighbor_node) in neighbors {
                    let current_received_time = SignalReceived::Time(cost + neighbor_cost);
                    
                    if received_signals[(*neighbor_node - 1) as usize] > current_received_time {
                        received_signals[(*neighbor_node - 1) as usize] = current_received_time;
                        
                        heap.push((cost + neighbor_cost, *neighbor_node));
                    }
                }
            }
        }

    }

    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
        let mut graph: HashMap<i32, Vec<Edge>> = HashMap::new();
        
        for node in &times {
            graph.entry(node[0])
                 .or_insert(vec![])
                 .push((node[2], node[1]));
        }


        let mut received_signals: Vec<SignalReceived> = vec![SignalReceived::Infinity; n as usize];
        received_signals[(k - 1) as usize] = SignalReceived::Time(0);

        Solution::calculate(&graph, k, &mut received_signals);

        return match received_signals.iter().max() {
            None => -1,
            Some(SignalReceived::Infinity) => -1,
            Some(SignalReceived::Time(time)) => *time,
        };
    }
}