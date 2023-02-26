# https://leetcode.com/problems/linked-list-cycle-ii
from typing import Optional

from leet.structures import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
