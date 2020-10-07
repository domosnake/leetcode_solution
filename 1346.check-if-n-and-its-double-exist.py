#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#
from typing import List


# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        double = set()
        half = set()
        for n in arr:
            if n in double or n in half:
                return True
            double.add(n * 2)
            if n % 2 == 0:
                half.add(n // 2)

        return False


# @lc code=end
