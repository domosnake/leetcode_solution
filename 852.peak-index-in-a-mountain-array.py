#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
from typing import List


# @lc code=start
class Solution:
    def peakIndexInMountainArray_linear(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return i

        return -1

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 1
        hi = len(arr) - 2
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            # peak on right
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid

        return lo


# s = Solution()
# arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
# a = s.peakIndexInMountainArray(arr)
# print(a)

# @lc code=end
