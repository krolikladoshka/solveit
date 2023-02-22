# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional

from leet.structures import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        walk = headA
        prev = walk
        while walk:
            prev = walk
            walk = walk.next
        prev.next = headA

        slow = headB
        fast = headB

        cycle = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast or headB.next is None:
            prev.next = None

            return None

        slow = headB
        while slow != fast:
            slow = slow.next
            fast = fast.next
        prev.next = None

        return fast
