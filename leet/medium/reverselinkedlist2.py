# https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

from leet.structures import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head
        cnt = 0
        prev = None
        walk = head
        while walk and cnt < left - 1:
            prev = walk
            walk = walk.next
            cnt += 1
        cd = right - left
        rev_head = walk
        pre_head = prev
        while walk and cd >= 0:
            next = walk.next
            walk.next = prev
            prev = walk
            walk = next
            cd -= 1
        if pre_head:
            pre_head.next = prev
        else:
            head = prev
        rev_head.next = walk

        return head
