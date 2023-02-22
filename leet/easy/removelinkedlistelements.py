# https://leetcode.com/problems/remove-linked-list-elements
from typing import Optional

from leet.structures import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre_head = ListNode(val=-1, next=head)
        prev = pre_head
        walk = head

        while walk:
            while walk and walk.val == val:
                prev.next = walk.next
                walk = walk.next
            if walk:
                prev = walk
                walk = walk.next
        return pre_head.next
