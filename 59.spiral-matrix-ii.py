#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List


# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        if n <= 0:
            return matrix
        # pre build matrix
        for _ in range(n):
            matrix.append([-1] * n)
        # lets go
        r = 0
        c = 0
        # 1 = right, 2 = down, 3 = left, 4 = up
        direction = 1
        for i in range(n * n):
            matrix[r][c] = i + 1
            if direction == 1:
                if self.hitWall(r, c + 1, matrix):
                    direction = 2
                    r += 1
                else:
                    c += 1
            elif direction == 2:
                if self.hitWall(r + 1, c, matrix):
                    direction = 3
                    c -= 1
                else:
                    r += 1
            elif direction == 3:
                if self.hitWall(r, c - 1, matrix):
                    direction = 4
                    r -= 1
                else:
                    c -= 1
            else:
                if self.hitWall(r - 1, c, matrix):
                    direction = 1
                    c += 1
                else:
                    r -= 1
        return matrix

    def hitWall(self, r: int, c: int, matrix: List[List[int]]) -> bool:
        # out of bounds
        if not (0 <= r < len(matrix) and 0 <= c < len(matrix)):
            return True
        # hit a filled cell
        else:
            return matrix[r][c] != -1


# @lc code=end
