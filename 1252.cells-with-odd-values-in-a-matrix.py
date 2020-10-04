#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#
from typing import List


# @lc code=start
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # row = n, col = m
        matrix = [[0] * m for _ in range(n)]
        for i in indices:
            for c in range(m):
                matrix[i[0]][c] += 1
            for r in range(n):
                matrix[r][i[1]] += 1
        count = 0
        for r in range(n):
            for c in range(m):
                if matrix[r][c] % 2 != 0:
                    count += 1
        return count


# @lc code=end
