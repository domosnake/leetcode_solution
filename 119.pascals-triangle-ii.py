#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
from typing import List


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]
        cur_row = []
        for _ in range(rowIndex):
            cur_row = []
            # left-end
            cur_row.append(1)
            # mid
            for j in range(1, len(prev_row)):
                cur_row.append(prev_row[j] + prev_row[j - 1])
            # right end
            cur_row.append(1)
            prev_row = cur_row
        return prev_row


# @lc code=end
