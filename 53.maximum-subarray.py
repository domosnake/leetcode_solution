#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp - store local sum and global max
        cur_sum = 0
        max_sum = float('-inf')
        # if we were to return such subarray, we could use below variables
        i = 0
        lo = 0
        hi = 0
        for j, num in enumerate(nums):
            # if local max can further increase max sum, add next num
            if cur_sum >= 0:
                cur_sum += num
            # if not, start new local max at next num, and set local start index
            else:
                cur_sum = num
                i = j
            # update max sum
            if cur_sum > max_sum:
                max_sum = cur_sum
                lo = i
                hi = j
        # tuple(maxSubarray, sum of maxSubarray)
        res = (nums[lo: hi + 1], max_sum)
        # we could return either maxSubarray or maxSum or both
        # for this probelm, let's return maxSum
        return res[1]


# @lc code=end
