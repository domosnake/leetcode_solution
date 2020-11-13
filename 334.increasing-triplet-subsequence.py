#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
from typing import List


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # subsequence, not subarray
        if not nums or len(nums) < 3:
            return False
        lo = float('inf')
        mid = float('inf')
        for n in nums:
            if n <= lo:
                lo = n
            elif n <= mid:
                mid = n
            else:
                return True
        return False


# s = Solution()
# a = s.increasingTriplet([1, 1, 2, 0, 3])
# print(a)

# @lc code=end
