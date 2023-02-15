# https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from collections import deque


class NestedInteger:
    def isInteger(self) -> bool:
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

    def getInteger(self) -> int:
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

    def getList(self) -> ['NestedInteger']:
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_list = []
        self.iterate_nested_list(nestedList)
        self.index = 0

    def next(self) -> int:
        value = self.flatten_list[self.index]
        self.index += 1

        return value

    def iterate_nested_list(self, nested_list: [NestedInteger]):
        for nested_integer in nested_list:
            if nested_integer.isInteger():
                self.flatten_list.append(nested_integer.getInteger())
            else:
                self.iterate_nested_list(nested_integer.getList())

    def hasNext(self) -> bool:
        return self.index <= len(self.flatten_list) - 1

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
