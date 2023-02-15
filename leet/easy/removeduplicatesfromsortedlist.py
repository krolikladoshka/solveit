# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional

from leet.structures import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    @linked_list_to_list
    @list_to_linked_list
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        walk = head
        while walk is not None and walk.next is not None:
            if walk.val != walk.next.val:
                walk = walk.next
            else:
                walk.next = walk.next.next
        return head

    @linked_list_to_list
    @list_to_linked_list
    def deleteDuplicates_dirty(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head

        prehead = ListNode(val=head.val - 1, next=head)
        current = head.val - 1
        walk = head
        prev = prehead
        while walk is not None:
            if walk.val != current:
                current = walk.val
                prev = walk
                walk = walk.next
            else:
                next = walk.next
                prev.next = next
                walk.next = None
                walk = next
        return prehead.next


