#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
from typing import List


# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        pairs = 0
        for v in count.values():
            pairs += v * (v - 1) // 2
        return pairs


# @lc code=end
