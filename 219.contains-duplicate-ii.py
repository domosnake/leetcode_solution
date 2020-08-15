#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
from typing import List


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # value to index map
        map = {}
        for i, n in enumerate(nums):
            if n in map and abs(map[n] - i) <= k:
                return True
            map[n] = i
        return False


# @lc code=end
