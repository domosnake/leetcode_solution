#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # one scan to check current and the next element
        # replace index start at 1, because index 0 is sorted
        # if cur != next, replace and increament index
        # if cur == next, keep scaning
        # key idea is to scan for unique item and put it to front
        sorted_tail = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[sorted_tail] = nums[i + 1]
                sorted_tail += 1
        return sorted_tail


# @lc code=end
