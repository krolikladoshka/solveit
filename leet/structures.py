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


def linked_list_to_list(fn):
    def convert(head: ListNode):
        while head is not None:
            yield head.val
            head = head.next

    @wraps(fn)
    def dec(*args, **kwargs):
        return list(convert(fn(*args, **kwargs)))

    return dec


def create_linked_list(lst) -> Optional[ListNode]:
    if lst:
        first = ListNode(lst[0])
        current = first
        for i in range(1, len(lst)):
            node = ListNode(lst[i])
            current.next = node
            current = node

        return first


def list_to_linked_list(fn):
    @wraps(fn)
    def dec(*args, **kwargs):
        self, *args = args
        return fn(self, *[
            create_linked_list(arg) if isinstance(arg, list) else arg
            for arg in args
        ], **kwargs)

    return dec


def list_of_lists_to_list_of_linked_lists(fn):
    @wraps(fn)
    def dec(*args, **kwargs):
        self, *args = args
        res_args = []

        for arg in args:
            if isinstance(arg, list):
                res_args.append(
                    [create_linked_list(lst) for lst in arg]
                )
            else:
                res_args.append(arg)

        return fn(self, *res_args, **kwargs)

    return dec


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        lval = self.left.val if self.left else None
        rval = self.right.val if self.right else None

        return f'TreeNode(val={self.val}, left=TreeNode(val={lval}), ' \
               f'right=TreeNode(val={rval}))'

    def __str(self):
        lval = self.left.val if self.left else None
        rval = self.right.val if self.right else None

        return f'val={self.val}, left={lval}, right={rval}'

# TODO: conversion is ambiguous
# def list_to_tree(fn):
#     def create_tree(lst):
#         if lst:
#             root = TreeNode(val=lst[0])
#             current = root
#             for i in range(1, len(lst)):
#                 current.left =
#                 node = ListNode(lst[i])
#                 current.next = node
#                 current = node
#
#             return first
#
#     @wraps(fn)
#     def dec(*args, **kwargs):
#         self, *args = args
#         return fn(self, *[
#             create_list(arg) for arg in args
#         ], **kwargs)
#
#     return dec
