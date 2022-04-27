#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        rotated = False
        while pivot < len(nums) - 1:
            if nums[pivot] > nums[pivot + 1]:
                rotated = True
                break
            pivot += 1
        # no pivot
        if not rotated:
            return self._binary_search(nums, target, 0, len(nums) - 1)
        # before pivot
        i = self._binary_search(nums, target, 0, pivot)
        # after pivot
        j = self._binary_search(nums, target, pivot + 1, len(nums) - 1)
        if i >= 0:
            return i
        elif j >= 0:
            return j
        else:
            return -1

    def _binary_search(self, nums, target, lo, hi):
        if target < nums[lo] or target > nums[hi]:
            return -1
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                return mid
        return -1


# s = Solution()
# a = [3, 1]
# b = 1
# print(s.search(a, b))
# @lc code=end
