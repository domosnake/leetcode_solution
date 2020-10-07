#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#
from typing import List


# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = arr[-1]
        arr[-1] = -1
        for i in reversed(range(len(arr) - 1)):
            temp = arr[i]
            arr[i] = cur_max
            cur_max = max(temp, arr[i])
        return arr


# @lc code=end
