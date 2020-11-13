#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List


# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        t = 0
        left = 0
        right = 0
        minLen = float('inf')
        while left < len(nums):
            # also check index range
            if t < s and right < len(nums):
                t += nums[right]
                right += 1
            elif t >= s:
                minLen = min(minLen, right - left)
                t -= nums[left]
                left += 1
            # reach end
            else:
                break
        if minLen == float('inf'):
            return 0
        return minLen


# s = Solution()
# a = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
# print(a)
# @lc code=end
