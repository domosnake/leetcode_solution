#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#
from typing import List


# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            s = str(i) + str(n-i)
            if '0' not in s:
                return [i, n - i]
        return []


# @lc code=end
