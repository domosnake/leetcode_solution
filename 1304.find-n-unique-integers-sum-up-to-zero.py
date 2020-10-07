#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#
from typing import List


# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n < 0:
            return []

        res = []
        while n > 1:
            res.extend([n, -n])
            n -= 2
        if n == 1:
            res.append(0)
        return res


# @lc code=end
