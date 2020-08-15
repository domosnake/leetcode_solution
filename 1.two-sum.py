#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # one pass map
        map = {}
        for i in range(len(nums)):
            # when looping, search in map for complement
            if nums[i] in map:
                return [map[nums[i]], i]
            # if not found, add the current element to map
            else:
                map[target - nums[i]] = i
        return [-1, -1]


# @lc code=end
