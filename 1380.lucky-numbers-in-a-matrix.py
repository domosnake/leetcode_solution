#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#
from typing import List


# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # lucky = min in row and max in col
        mins = set()
        for row in matrix:
            mins.add(min(row))
        maxs = set()
        for col in zip(*matrix):
            maxs.add(max(col))
        return list(maxs.intersection(mins))


# @lc code=end
