#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#
from typing import List


# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int],
                    queryTime: int) -> int:
        if not startTime or not endTime or queryTime < 1:
            return 0
        students = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                students += 1
        return students


# @lc code=end
