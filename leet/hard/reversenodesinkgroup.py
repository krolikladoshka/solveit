# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import Optional

from leet.structures import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if head.next is None:
            return head
        if k <= 1:
            return head

        prehead = ListNode(-1)
        prehead.next = head
        pre_start = prehead
        start = walk = head
        counter = 0
        while walk is not None:
            counter += 1
            if counter >= k:
                next = walk.next
                pre_start.next = None
                walk.next = None
                r_head, r_tail = self.reverse_list(start)
                pre_start.next = r_head
                r_tail.next = next
                pre_start = prev = r_tail
                start = next
                walk = r_tail
                counter = 0
            if walk:
                walk = walk.next
        return prehead.next

    def reverse_list(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        if not head or not head.next:
            return head, None
        prev = None
        tail = head
        next = head.next
        while head:
            head.next = prev
            prev = head
            head = next

            if next:
                next = next.next
        return prev, tail
