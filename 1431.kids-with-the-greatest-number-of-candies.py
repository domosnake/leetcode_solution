#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#
from typing import List


# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int],
                        extraCandies: int) -> List[bool]:
        if not candies:
            return []
        res = [False] * len(candies)
        max_candy = max(candies)
        for i, c in enumerate(candies):
            res[i] = c + extraCandies >= max_candy
        return res


# @lc code=end
