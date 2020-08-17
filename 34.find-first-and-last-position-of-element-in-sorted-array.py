#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        targetRange = [-1, -1]
        # init low and hi
        low = 0
        hi = len(nums) - 1
        # search start position of range
        while low < hi:
            # biased to mid-left
            mid = low + (hi - low) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                hi = mid
        if nums[low] == target:
            targetRange[0] = low

        # init hi
        hi = len(nums) - 1
        # search end position of range
        while low < hi:
            # biased to mid-right
            mid = low + ((hi - low) // 2) + 1
            if target < nums[mid]:
                hi = mid - 1
            else:
                low = mid
        if nums[hi] == target:
            targetRange[1] = hi
        return targetRange


# @lc code=end
