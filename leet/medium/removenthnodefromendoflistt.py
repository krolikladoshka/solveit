# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional

from leet.structures import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            if n == 1:
                return None
            return head
        pre_head = ListNode(-1, head)
        first = pre_head
        second = pre_head

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return pre_head.next
