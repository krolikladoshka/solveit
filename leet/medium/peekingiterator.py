# https://leetcode.com/problems/peeking-iterator/description/
# Below is the interface for Iterator, which is already defined for you.
#
from collections import deque


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class Peeker:
    def __init__(self, value=None, has_value=False):
        self.value = value
        self.has_value = has_value


class PeekingIterator:

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peeker = Peeker()
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.peeker.has_value:
            self.peeker.value, self.peeker.has_value = self.next(), True
        return self.peeker.value

    def next(self):
        """
        :rtype: int
        """
        if self.peeker.has_value:
            self.peeker.has_value = False
            return self.peeker.value
        next = self.iterator.next()
        return next

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeker.has_value or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
