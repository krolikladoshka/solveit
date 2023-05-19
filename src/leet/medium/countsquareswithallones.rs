// https://leetcode.com/problems/count-square-submatrices-with-all-ones/
pub struct Solution;

impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        let mut dp = vec![
            vec![0; matrix[0].len()];
            matrix.len()
        ];

        for i in 0..matrix.len() {
            for j in 0..matrix[0].len() {
                if matrix[i][j] == 1 {
                    if i == 0 || j == 0 {
                        dp[i][j] = 1;
                    } else {
                        let vals = [dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]];
                        dp[i][j] = vals.iter().min().unwrap() + 1; 
                    }
                }
            }
        }

        return dp.iter().flatten().sum();
    }
}