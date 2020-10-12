#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#
from typing import List


# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = nums[:]
        for i in range(1, len(running_sum)):
            running_sum[i] = running_sum[i - 1] + running_sum[i]
        return running_sum


# @lc code=end
