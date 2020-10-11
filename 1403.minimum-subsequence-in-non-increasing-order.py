#
# @lc app=leetcode id=1403 lang=python3
#
# [1403] Minimum Subsequence in Non-Increasing Order
#
from typing import List


# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) < 2:
            return nums
        nums.sort(reverse=True)
        total_sum = sum(nums)
        sub_sum = 0
        sub = []
        for n in nums:
            sub.append(n)
            sub_sum += n
            if sub_sum > total_sum - sub_sum:
                return sub
        return []


# @lc code=end
