# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional

from leet.structures import ListNode, linked_list_to_list, list_of_lists_to_list_of_linked_lists


class Solution:
    @linked_list_to_list
    @list_of_lists_to_list_of_linked_lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) <= 1:
            return lists[0]

        step = 1
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i] = self.merge_two_sorted_lists(lists[i], lists[i + step])
            step *= 2
        return lists[0]

    @linked_list_to_list
    @list_of_lists_to_list_of_linked_lists
    def mergeKLists_nsquared(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) <= 1:
            return lists[0]
        res = None

        for lst in lists:
            res = self.merge_two_sorted_lists(res, lst)
        return res

    def merge_two_sorted_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
