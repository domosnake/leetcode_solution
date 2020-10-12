#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#
from typing import List


# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        top = float('-inf')
        bottom = float('inf')
        for s in salary:
            top = max(top, s)
            bottom = min(bottom, s)
            total += s
        return (total - top - bottom) / (len(salary) - 2)


# @lc code=end
