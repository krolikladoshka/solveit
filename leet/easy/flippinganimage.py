# https://leetcode.com/problems/flipping-an-image
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            start = 0
            end = len(image[i]) - 1

            while start < end:
                image[i][start], image[i][end] = image[i][end] ^ 1, image[i][start] ^ 1
                start += 1
                end -= 1
            if start == end:
                image[i][start] ^= 1
        return image
