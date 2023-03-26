use leet::medium::rottingoranges::Solution;
mod leet;

fn main() {
    let args = vec![
        vec![vec![2,1,1], vec![1,1,0], vec![0,1,1]],
        vec![vec![2,1,1], vec![0,1,1], vec![1,0,1]],
        vec![vec![2,1,1], vec![1,1,1], vec![0,1,2]],
    ];
    // let arg = vec![vec![2,1,1], vec![1,1,0], vec![0,1,1]];
    // let arg = vec![vec![2,1,1], vec![0,1,1], vec![1,0,1]];
    // let arg = vec![vec![2,1,1], vec![1,1,1], vec![0,1,2]];

    for arg in args {
        println!("{0}", Solution::oranges_rotting(arg));
    }
}