#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#
from typing import List


# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            count += 1 if len(str(n)) % 2 == 0 else 0
        return count


# @lc code=end
