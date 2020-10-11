#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Sub-arrays
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if not target or not arr:
            return False
        # if you can select any non-empty sub-array and reverse it
        # then you can reorder the arr any way you want
        # so that problem becomes do we have all elements of target in arr?
        count = defaultdict(int)
        for i in range(len(target)):
            count[target[i]] -= 1
            count[arr[i]] += 1
        for v in count.values():
            if v != 0:
                return False
        return True


# @lc code=end
