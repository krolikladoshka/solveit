from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        def can_fill(x, y, c):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            return image[x][y] == c

        def fill(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if image[x][y] == color:
                return

            cell_color = image[x][y]
            image[x][y] = color
            for direction in directions:
                xf, yf = x + direction[0], y + direction[1]
                if can_fill(xf, yf, cell_color):
                    fill(xf, yf)


        fill(sr, sc)

        return image
