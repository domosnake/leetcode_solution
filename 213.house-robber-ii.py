#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # subproblem 1: rob first house
        rob_first = 0
        prev_1 = 0
        prev_2 = 0
        for j in range(len(nums) - 1):
            rob_first = max(prev_2 + nums[j], prev_1)
            prev_2 = prev_1
            prev_1 = rob_first
        # subproblem 2: not rob first house
        not_rob_first = 0
        prev_1 = 0
        prev_2 = 0
        for j in range(1, len(nums)):
            not_rob_first = max(prev_2 + nums[j], prev_1)
            prev_2 = prev_1
            prev_1 = not_rob_first
        # combine 2 subs, get the larger one
        return max(rob_first, not_rob_first)


# @lc code=end
