#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea_brute_force(self, height: List[int]) -> int:
        # brute force
        maxWater = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                maxWater = max(maxWater, w * h)
        return maxWater

    def maxArea(self, height: List[int]) -> int:
        # 2 pointer shrink
        lo = 0
        hi = len(height) - 1
        maxWater = 0
        while lo < hi:
            # move shorter pointer => may increase area
            if height[lo] < height[hi]:
                maxWater = max(maxWater, (hi - lo) * height[lo])
                lo += 1
            else:
                maxWater = max(maxWater, (hi - lo) * height[hi])
                hi -= 1
        return maxWater


# @lc code=end
