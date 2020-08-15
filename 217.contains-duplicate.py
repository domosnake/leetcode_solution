#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # similar idea, but this time we are comparing size
        my_set = set(nums)
        return len(nums) != len(my_set)
        

# @lc code=end
