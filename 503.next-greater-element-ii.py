#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
from typing import List


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # circular array
        stack = []
        res = [-1] * len(nums)
        # imagine we have 2 arrays
        for i in reversed(range(2 * len(nums))):
            n = nums[i % len(nums)]
            while stack and stack[-1] <= n:
                stack.pop()
            if stack:
                res[i % len(nums)] = stack[-1]
            stack.append(n)
        return res


# @lc code=end
