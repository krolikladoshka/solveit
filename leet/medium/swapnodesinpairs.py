# https://leetcode.com/problems/swap-nodes-in-pairs

from typing import Optional

from leet.structures import ListNode, linked_list_to_list, list_to_linked_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.next is None:
            return head

        prehead = ListNode(-1)
        prehead.next = head
        prev = prehead
        walk = head
        while walk is not None and walk.next is not None:
            first = walk
            second = walk.next
            nx = second.next
            prev.next = second
            first.next = nx
            second.next = first
            prev = first
            walk = nx
        return prehead.next