// https://leetcode.com/problems/house-robber-iii/

use std::rc::Rc;
use std::cell::RefCell;
use std::cmp::max;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

type WeakTree = Option<Rc<RefCell<TreeNode>>>;

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None
        }
    }
}

pub struct Solution;

impl Solution {
    fn rob_houses_dfs(node: WeakTree) -> (i32, i32) {
        match node {
            Some(node) => {
                let (rob_left, not_rob_left) = Solution::rob_houses_dfs(node.borrow().left.clone());
                let (rob_right, not_rob_right) = Solution::rob_houses_dfs(node.borrow().right.clone());

                let rob = node.borrow().val + not_rob_left + not_rob_right;
                let not_rob = max(rob_left, not_rob_left) + max(rob_right, not_rob_right);

                return (rob, not_rob);
            },
            None => {
                return (0, 0);
            }
        }
    }

    pub fn rob(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (rob, not_rob) = Solution::rob_houses_dfs(root);

        return max(rob, not_rob);
    }
}