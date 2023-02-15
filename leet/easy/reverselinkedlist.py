# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

from leet.structures import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        rev_head = None
        while head:
            next = head.next
            head.next = rev_head
            rev_head = head
            head = next
        return rev_head

    @linked_list_to_list
    @list_to_linked_list
    def reverse_list_dirty(self, head: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        if not head or not head.next:
            return head
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
