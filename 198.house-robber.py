#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


# @lc code=start
class Solution:
    def rob_dp(self, nums: List[int]) -> int:
        # O(n) space
        # rob current => rob[i] = rob[i - 2] + cur
        # not rub current => rob[i] = rob[i - 1]
        rob = [0] * (len(nums) + 2)
        i = 2
        for n in nums:
            rob_cur = rob[i - 2] + n
            not_rob_cur = rob[i - 1]
            rob[i] = max(rob_cur, not_rob_cur)
            i += 1
        return rob[-1]

    def rob(self, nums: List[int]) -> int:
        # O(1) space
        # rob current => rob[i] = rob[i - 2] + cur
        # not rub current => rob[i] = rob[i - 1]
        # for each house, decide max(rob current, not rob current)
        cur = 0
        prev = 0
        prev_prev = 0
        for n in nums:
            cur = max(prev_prev + n, prev)
            prev_prev = prev
            prev = cur
        return cur

# @lc code=end
