#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp - store local and global max
        localMax = 0
        globalMax = float('-inf')
        # if we were to return such subarray, we could use below variables
        localStart = 0
        globalStart = 0
        globalEnd = 0
        for i, num in enumerate(nums):
            # if local max can further increase max sum, add next num
            if localMax >= 0:
                localMax += num
            # if not, start new local max at next num, and set local start index
            else:
                localMax = num
                localStart = i
            # update max sum
            if localMax > globalMax:
                globalMax = localMax
                globalStart = localStart
                globalEnd = i
        # tuple(maxSubarray, sum of maxSubarray)
        res = (nums[globalStart: globalEnd + 1], globalMax)
        # we could return either maxSubarray or maxSum or both
        # for this probelm, let's return maxSum
        return res[1]


# @lc code=end
