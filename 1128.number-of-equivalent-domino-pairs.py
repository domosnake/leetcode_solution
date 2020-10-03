#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#
from typing import List


# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        for d in dominoes:
            t = (d[0], d[1])
            _t = (d[1], d[0])
            if t in count:
                count[t] += 1
            elif _t in count:
                count[_t] += 1
            else:
                count[t] = 1
        pairs = 0
        for p in count.values():
            if p > 1:
                pairs += p * (p - 1) // 2
        return pairs


# @lc code=end
