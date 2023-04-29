// https://leetcode.com/problems/reverse-linked-list/

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

pub struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if let Some(start) = head {
            let mut head = None;
            let mut current = start;
            loop {
                current.next = head;
                head = Some(current);
            }
            return head;  

        }
        return None;
    }
}