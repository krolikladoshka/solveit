# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list
from leet.structures import ListNode


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 0:
            return None

        pre_head = ListNode(val=-1, next=head)
        walk = head
        prev = pre_head
        while walk:
            walk_counter = 0
            while walk_counter < m and walk:
                prev = walk
                walk = walk.next
                walk_counter += 1
            if not walk:
                break
            remove_counter = 0
            while remove_counter < n and walk:
                walk = walk.next
                remove_counter += 1
            prev.next = walk
        return pre_head.next
