# https://leetcode.com/problems/merge-two-sorted-lists/
from functools import wraps
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f'ListNode(val={self.val})'


def convert_to_list(fn):
    def convert(head: ListNode):
        while head is not None:
            yield head.val
            head = head.next

    @wraps(fn)
    def dec(*args, **kwargs):
        return list(convert(fn(*args, **kwargs)))

    return dec


class Solution:
    @convert_to_list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = self.create_list(list1)
        list2 = self.create_list(list2)

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = ListNode(float('-inf'))
        result = head

        while list1 is not None and list2 is not None:
            current = list1
            while current is not None and current.val <= list2.val:
                result.next = current
                result = result.next
                current = current.next
            list1 = current
            list1, list2 = list2, list1
        if list1 is not None:
            result.next = list1
        if list2 is not None:
            result.next = list2
        real_head = head.next
        head.next = None
        return real_head

    def create_list(self, lst):
        if lst:
            first = ListNode(lst[0])
            current = first
            for i in range(1, len(lst)):
                node = ListNode(lst[i])
                current.next = node
                current = node

            return first
