#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#
from typing import List


# @lc code=start
class Solution:
    def maxProduct_sort(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return -1
        nums.sort()
        # time: O(nlogn)
        return (nums[-1] - 1) * (nums[-2] - 1)

    def maxProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return -1
        n1 = -1
        n2 = -1
        index = 0
        for i, n in enumerate(nums):
            if n > n1:
                n1 = n
                index = i
        nums[index] = -1
        n2 = max(nums)
        # time: O(n)
        return (n1 - 1) * (n2 - 1)


# @lc code=end
