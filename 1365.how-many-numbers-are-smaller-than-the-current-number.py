#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#
from typing import List


# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        order = sorted(nums)
        table = {}
        for i, n in enumerate(order):
            if n not in table:
                table[n] = i
        res = []
        for n in nums:
            res.append(table[n])

        return res


# @lc code=end
