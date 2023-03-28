// class Solution:
//     def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
//         sm = 0
//         sm += min(numOnes, k)

//         k -= sm 

//         if k <= 0:
//             return sm
//         k -= numZeros
//         if k <= 0:
//             return sm
//         sm -= min(numNegOnes, k)

//         return sm 
pub struct Solution;

impl Solution {
    pub fn k_items_with_maximum_sum(num_ones: i32, num_zeros: i32, num_neg_ones: i32, k: i32) -> i32 {
        use std::cmp::min;
        let mut k = k;
        
        let mut sum = min(num_ones, k);
        
        k -= sum;

        if k <= 0 {
            return sum;
        }

        k -= num_zeros;

        if k <= 0 {
            return sum;
        }

        return  sum - min(num_neg_ones, k);
    }
}