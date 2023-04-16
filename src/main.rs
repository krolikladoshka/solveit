mod leet;
mod smallapps;
use leet::medium::countnodeswiththehighestscore;
use smallapps::emulators::{dendynes::dendy_run};

fn main() {
    // let args = vec![
    //     vec![vec![2,1,1], vec![1,1,0], vec![0,1,1]],
    //     vec![vec![2,1,1], vec![0,1,1], vec![1,0,1]],
    //     vec![vec![2,1,1], vec![1,1,1], vec![0,1,2]],
    // ];
    // let arg = vec![vec![2,1,1], vec![1,1,0], vec![0,1,1]];
    // let arg = vec![vec![2,1,1], vec![0,1,1], vec![1,0,1]];
    // let arg = vec![vec![2,1,1], vec![1,1,1], vec![0,1,2]];
    // let args = vec![
    //     (vec![vec![2,1,1], vec![2,3,1], vec![3,4,1]], 4, 2),
    //     (vec![vec![1,2,1]], 2, 1),
    //     (vec![vec![1,2,1]], 2, 2),
    // ];
    // let args = vec![
    //     vec![vec![1,1], vec![1,0]],
    //     vec![vec![1,1], vec![1,1]],
    //     vec![
    //         vec![1, 1, 0, 1, 1],
    //         vec![0, 1, 0, 1, 0],
    //         vec![0, 0, 1, 1, 0],
    //         vec![1, 1, 0, 0, 0],
    //         vec![0, 1, 1, 0, 0],
    //     ]
    // ];
    // for arg in args {
    //     let result = Solution::largest_island(arg);
    //     // for row in &result {
    //     //     println!("{:?}", row);
    //     // }
    //     println!("{}", result);
    //     // println!("{0}", Solution::network_delay_time(arg.0, arg.1, arg.2));
    // }
    // dendy_run();
    // chip8_run();
    countnodeswiththehighestscore::Solution::count_highest_score_nodes(vec![-1,2,0,2,0]);
}