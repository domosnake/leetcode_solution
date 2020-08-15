#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]
        cur_row = []
        for i in range(1, numRows):
            cur_row = []
            # left end
            cur_row.append(1)
            # mid
            for j in range(1, len(res[-1])):
                cur_row.append(res[-1][j] + res[-1][j - 1])
            # right end
            cur_row.append(1)
            res.append(cur_row)
        return res


# @lc code=end
