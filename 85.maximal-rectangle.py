#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
from typing import List


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        area = 0
        height = [0] * len(matrix[0])
        for r in range(len(matrix)):
            # build a histogram on each row
            for c in range(len(height)):
                if matrix[r][c] == '0':
                    height[c] = 0
                else:
                    height[c] += 1

            area = max(area, self.largestRectangleArea(height))
        return area

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # monotonic stack
        # time: O(n)
        # space: O(n)

        # sentinel at head and tail
        guard_heights = [0] + heights + [0]
        area = -1
        # store index
        stack = [0]
        for i in range(1, len(guard_heights)):
            while guard_heights[stack[-1]] > guard_heights[i]:
                h = guard_heights[stack.pop()]
                d = i - stack[-1] - 1
                area = max(area, d * h)
            stack.append(i)
        return area


# s = Solution()
# m = [["1", "0", "1", "0", "0"],
#      ["1", "0", "1", "1", "1"],
#      ["1", "1", "1", "1", "1"],
#      ["1", "0", "0", "1", "0"]]
# a = s.maximalRectangle(m)
# print(a)

# @lc code=end
