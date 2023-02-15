from typing import Optional

from leet.structures import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
