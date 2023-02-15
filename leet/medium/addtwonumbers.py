# https://leetcode.com/problems/add-two-numbers/
from typing import Optional

from leet.structures import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        dec = 0
        result_head = ListNode(val=0)
        result = result_head

        while True:
            d_l1 = l1.val if l1 else 0
            d_l2 = l2.val if l2 else 0
            val = d_l1 + d_l2 + dec
            dec = val // 10
            result.next = ListNode(val=val % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result = result.next
            if not l1 and not l2:
                if dec != 0:
                    result.next = ListNode(val=dec)
                return result_head.next
