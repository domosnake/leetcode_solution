#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#
from typing import List


# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target or n < 1:
            return []
        tgt = set(target)
        ops = []
        i = 1
        while tgt:
            ops.append('Push')
            if i not in tgt:
                ops.append('Pop')
            tgt.discard(i)
            i += 1
        return ops

    def buildArray_better_space(self, target: List[int], n: int) -> List[str]:
        if not target or n < 1:
            return []
        j = 0
        ops = []
        for i in range(1, target[-1] + 1):
            ops.append('Push')
            if i == target[j]:
                j += 1
            else:
                ops.append('Pop')
        return ops


# @lc code=end
