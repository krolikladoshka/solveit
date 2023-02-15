# https://leetcode.com/problems/linked-list-cycle
from typing import Optional

from leet.structures import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
