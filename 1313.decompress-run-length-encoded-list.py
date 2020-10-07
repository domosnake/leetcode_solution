#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#
from typing import List


# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # [freq, val] = [nums[2*i], nums[2*i+1]]
        decompressed = []
        for i in range(0, len(nums), 2):
            decompressed.extend([nums[i + 1]] * nums[i])
        return decompressed


# @lc code=end
