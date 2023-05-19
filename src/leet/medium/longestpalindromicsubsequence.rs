// https://leetcode.com/problems/longest-palindromic-subsequence

pub struct Solution;

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        fn longest_common_subsequence(text1: String, text2: String) -> i32 {
            let mut dp = vec![
                vec![0; text1.len() + 1];
                text2.len() + 1
            ];
            
            for (i, c2) in (0..text2.len()).rev().zip(text2.chars().rev()) {
                for (j, c1) in (0..text1.len()).rev().zip(text1.chars().rev()) {
                    if c1 == c2 {
                        dp[i][j] = dp[i + 1][j + 1] + 1
                    } else {
                        dp[i][j] = std::cmp::max(dp[i + 1][j], dp[i][j + 1]);
                    }
                }
            }
            return dp[0][0];
        }

        return longest_common_subsequence(s.clone(), s.chars().rev().collect());
    }
}