pub struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut lowest_price = prices[0];
        let mut sum = 0;

        for i in 0..prices.len() {
            if lowest_price > prices[i] {
                lowest_price = prices[i];
            } else {
                sum = std::cmp::max(sum, sum + prices[i] - lowest_price); 
                lowest_price = prices[i];
            }
        }
        return sum;
    }
}