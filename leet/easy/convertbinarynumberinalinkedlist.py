# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
from leet.structures import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        result = 0
        while head:
            result = (result << 1) + head.val
            head = head.next

        return result
