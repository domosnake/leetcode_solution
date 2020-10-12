#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#
from typing import List


# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [''] * len(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        return ''.join(shuffled)


# @lc code=end
