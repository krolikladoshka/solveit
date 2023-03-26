use leet::medium::networkdelaytime::Solution;
mod leet;

fn main() {
    // let args = vec![
    //     vec![vec![2,1,1], vec![1,1,0], vec![0,1,1]],
    //     vec![vec![2,1,1], vec![0,1,1], vec![1,0,1]],
    //     vec![vec![2,1,1], vec![1,1,1], vec![0,1,2]],
    // ];
    // let arg = vec![vec![2,1,1], vec![1,1,0], vec![0,1,1]];
    // let arg = vec![vec![2,1,1], vec![0,1,1], vec![1,0,1]];
    // let arg = vec![vec![2,1,1], vec![1,1,1], vec![0,1,2]];
    let args = vec![
        (vec![vec![2,1,1], vec![2,3,1], vec![3,4,1]], 4, 2),
        (vec![vec![1,2,1]], 2, 1),
        (vec![vec![1,2,1]], 2, 2),
    ];
    
    for arg in args {
        println!("{0}", Solution::network_delay_time(arg.0, arg.1, arg.2));
    }
}