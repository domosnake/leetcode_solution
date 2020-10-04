#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#
from typing import List


# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        cycle = rows * cols
        k %= cycle
        list = []
        for r in range(rows):
            for c in range(cols):
                list.append(grid[r][c])

        self.reverseList(list, 0, cycle - 1)
        self.reverseList(list, 0, k - 1)
        self.reverseList(list, k, cycle - 1)

        res = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(list[r * cols + c])
            res.append(row)
        return res

    def reverseList(self, list, lo, hi):
        while lo < hi:
            list[lo], list[hi] = list[hi], list[lo]
            lo += 1
            hi -= 1

# @lc code=end
