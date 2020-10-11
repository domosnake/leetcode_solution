#
# @lc app=leetcode id=1413 lang=python3
#
# [1413] Minimum Value to Get Positive Step by Step Sum
#
from typing import List


# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if not nums:
            return -1
        res = 1
        step_sum = res
        for n in nums:
            step_sum += n
            if step_sum < 1:
                res += 1 - step_sum
                step_sum = 1
        return res


# @lc code=end
