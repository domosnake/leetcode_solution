#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from typing import List


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # similar to No.26 Remove Duplicates from Sorted Array
        # except we need to count number of duplicates
        # keep scanning once count exceeds threshold
        sorted_tail = 1
        count = 1
        # max number of duplicates can appear, e.g MAX_DUP = 4
        MAX_DUP = 2
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
                if count <= MAX_DUP:
                    nums[sorted_tail] = nums[i + 1]
                    sorted_tail += 1
            else:
                nums[sorted_tail] = nums[i + 1]
                sorted_tail += 1
                count = 1
        return sorted_tail


# @lc code=end
