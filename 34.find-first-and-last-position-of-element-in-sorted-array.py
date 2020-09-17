#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List
from enum import Enum


# @lc code=start
class Position(Enum):
    FIRST = 1
    LAST = 2


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first_pos = self.binarySearch(nums, target, Position.FIRST)
        last_pos = self.binarySearch(nums, target, Position.LAST)
        return [first_pos, last_pos]

    def binarySearch(self, nums: List[int], target: int, pos: Position) -> int:
        if not nums:
            return -1
        lo = 0
        hi = len(nums) - 1
        index = -1
        while lo <= hi:
            # avoid overflow
            mid = (hi - lo) // 2 + lo
            # binary search
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                index = mid
                if pos == Position.FIRST:
                    # keep reducing hi to find first index
                    hi = mid - 1
                elif pos == Position.LAST:
                    # keep expanding lo to find last index
                    lo = mid + 1
        return index


s = Solution()
a = s.searchRange([5, 7, 7, 8, 8, 8, 8, 10], 8)
print(a)
# @lc code=end
