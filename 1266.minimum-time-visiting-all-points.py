#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#
from typing import List


# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        time = 0
        for i in range(1, len(points)):
            start = points[i - 1]
            end = points[i]
            min_distance = max(abs(start[0] - end[0]), abs(start[1] - end[1]))
            time += min_distance
        return time


# @lc code=end
