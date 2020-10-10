#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
from typing import List


# @lc code=start
class Solution:
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

    def largestRectangleArea_all_areas(self, heights: List[int]) -> int:
        if not heights:
            return 0
        # monotonic stack
        # time: O(n)
        # space: O(n)

        # sentinel at head and tail
        guard_heights = [0] + heights + [0]
        areas = [0] * len(guard_heights)
        # store index
        stack = [0]
        for i in range(1, len(guard_heights)):
            while guard_heights[stack[-1]] > guard_heights[i]:
                j = stack.pop()
                h = guard_heights[j]
                d = i - stack[-1] - 1
                areas[j] = d * h
            stack.append(i)
        return max(areas)

    def largestRectangleArea_brute_force(self, heights: List[int]) -> int:
        # brute force
        # time: O(n^2)
        # space: O(1)
        area = -1
        for i, h in enumerate(heights):
            d = 1
            # search left
            for j in reversed(range(i)):
                if heights[j] >= h:
                    d += 1
                else:
                    break

            # search right
            for j in range(i + 1, len(heights)):
                if heights[j] >= h:
                    d += 1
                else:
                    break
            area = max(area, d * h)
        return area


# @lc code=end
