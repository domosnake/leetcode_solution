#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from typing import List


# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for n in arr:
            count[n] = count.get(n, 0) + 1

        unique = set()
        for v in count.values():
            if v in unique:
                return False
            unique.add(v)
        return True


# @lc code=end
