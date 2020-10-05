#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if not arr:
            return 0
        target = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if target == arr[i]:
                count += 1
            else:
                target = arr[i]
                count = 1
            if count > len(arr) / 4:
                break
        return target


# @lc code=end
