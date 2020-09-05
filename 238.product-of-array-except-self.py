#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # next term is the product of all prev terms
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        # backwards, next term is the product of all prev terms
        for i in reversed(range(len(nums))):
            res[i] *= right
            right *= nums[i]

        return res


# @lc code=end
