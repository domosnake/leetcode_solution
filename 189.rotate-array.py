#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # reverse: in-place O(n) space
        # rotation is periodic, only 1 round counts
        k %= len(nums)
        # reverse whole list
        self.reverse(nums, 0, len(nums) - 1)
        # reverse head
        self.reverse(nums, 0, k - 1)
        # reverse tail
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            # swap
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# @lc code=end
