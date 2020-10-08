#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#
from typing import List


# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1
        lucky = -1
        for k, v in count.items():
            if k == v:
                lucky = max(lucky, k)
        return lucky


# @lc code=end
