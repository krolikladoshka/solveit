# https://leetcode.com/problems/hamming-distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        counter = 0
        while xor:
            counter += xor & 1
            xor >>= 1
        return counter
