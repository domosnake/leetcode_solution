#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#
from typing import List


# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = len(arr1)
        for n1 in arr1:
            for n2 in arr2:
                if abs(n1 - n2) <= d:
                    res -= 1
                    break
        return res


# @lc code=end
