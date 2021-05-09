#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        lookup = set(nums)
        for n in lookup:
            # check one direction
            if n - 1 not in lookup:
                m = n + 1
                while m in lookup:
                    m += 1
                maxLen = max(maxLen, m - n)
        return maxLen


# @lc code=end
