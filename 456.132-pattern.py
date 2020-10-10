#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#
from typing import List


# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        next_smaller_element = float('-inf')
        for n in reversed(nums):
            # given that we have next smaller element of the peak
            if n < next_smaller_element:
                return True
            # find next smaller element of the peak
            while stack and stack[-1] < n:
                next_smaller_element = stack.pop()
            stack.append(n)
        return False


# @lc code=end
