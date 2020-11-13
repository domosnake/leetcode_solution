#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob current => rob[i] = rob[i - 2] + cur
        # not rub current => rob[i] = rob[i - 1]
        if not nums:
            return 0
        i = 0
        i_1 = 0
        i_2 = 0
        for n in nums:
            i = max(i_2 + n, i_1)
            i_2 = i_1
            i_1 = i
        return i


# @lc code=end
