#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        prod = 1

        # left to right
        for n in nums:
            prod *= n
            max_prod = max(max_prod, prod)
            if n == 0:
                prod = 1

        # reset prod
        prod = 1
        # right to left
        for n in nums[::-1]:
            prod *= n
            max_prod = max(max_prod, prod)
            if n == 0:
                prod = 1

        return max_prod


# s = Solution()
# a = s.maxProduct([2, 3, -2, 4, 1, 3])
# print(a)

# @lc code=end
