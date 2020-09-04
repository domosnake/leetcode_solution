#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # trap_dp is optimized, but we can even imporve space complexity further
        # note that the trapped water is determined by shorter wall on both sides
        # thus, if leftMax = 1, as long as rightMax > leftMax
        # the trapped water is always determined by leftMax
        # this means that we don't need track all leftMax and rightMax
        # therefore, reduce space to O(1)
        #
        # we use 2 pointers left and right to traverse the height from both ends
        total_water = 0
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        while left < right:
            # left wall is shorter
            if leftMax < rightMax:
                # water is determined by left
                total_water += leftMax - height[left]
                # move left
                left += 1
                # compute new leftMax
                leftMax = max(leftMax, height[left])
            # right wall is shorter
            else:
                total_water += rightMax - height[right]
                # move right
                right -= 1
                # update rightMax
                rightMax = max(rightMax, height[right])
        return total_water

    def trap_brute_force(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # for each i in height, the water trapped in i
        # is the shorter wall(max height) on both side of i, minus its height
        # thus, water(i) = min(max[0~i], max[i~n-1]) - height[i]
        # total water trapped is sum(water)
        # time: O(n^2) - for each i, scan the entire height list
        # space: O(1)
        total_water = 0
        for i, h in enumerate(height):
            leftMax = 0
            rightMax = 0
            # scan to find left max
            for x in range(0, i + 1):
                leftMax = max(leftMax, height[x])
            # scan to find right max
            for y in range(i, len(height)):
                rightMax = max(rightMax, height[y])
            # determined by shorter wall
            total_water += min(leftMax, rightMax) - h
        return total_water

    def trap_dp(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # same solution as brute force with optimization on time
        # pre-compute lists of leftMax and rightMax
        # time: O(n) - 2 passes to compute leftMax and rightMax, 1 pass to comptue water
        # space: O(n) - store lists of leftMax and rightMax
        total_water = 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        # pre-compute leftMax, leftMax is max[0~i]
        for x in range(n):
            if x == 0:
                leftMax[x] = height[x]
            else:
                leftMax[x] = max(leftMax[x - 1], height[x])
        # pre-compute rightMax, rightMax is max[i~n-1]
        for y in reversed(range(n)):
            if y == n - 1:
                rightMax[y] = height[y]
            else:
                rightMax[y] = max(rightMax[y + 1], height[y])

        for i, h in enumerate(height):
            # note that query for leftMax and rightMax is reduced to O(1)
            total_water += min(leftMax[i], rightMax[i]) - h
        return total_water


# @lc code=end
