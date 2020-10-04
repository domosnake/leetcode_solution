#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
from typing import List


# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates:
            return False
        if len(coordinates) < 3:
            return True
        # 3 points on the same line
        #  (y1 - y2) / (x1 - x2) = (y2 - y3) / (x2 - x3)
        #  (y1 - y2) * (x2 - x3) = (y2 - y3) * (x1 - x2)
        p1 = coordinates[0]
        p2 = coordinates[1]
        for i in range(2, len(coordinates)):
            p = coordinates[i]
            if (p1[1] - p2[1]) * (p2[0] - p[0]) != (p2[1] - p[1]) * (p1[0] - p2[0]):
                return False
        return True


# s = Solution()
# a = s.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
# print(a)

# @lc code=end
