#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        major = None
        major_count = -1
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > major_count:
                major = num
                major_count = map[num]
            # once major number is found, no need to continue
            if major_count > len(nums) / 2:
                break
        return major


# @lc code=end
