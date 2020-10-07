#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#
from typing import List


# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for row in grid:
            for i, v in enumerate(row):
                if v < 0:
                    neg += len(row) - i
                    break
        return neg


# @lc code=end
