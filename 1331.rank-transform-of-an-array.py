#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        val_to_index = defaultdict(list)
        for i, v in enumerate(arr):
            val_to_index[v].append(i)

        res = [0] * len(arr)
        rank = 1
        for v in sorted(arr):
            rank_up = 1
            for i in val_to_index[v]:
                if res[i] != 0:
                    rank_up = 0
                    break
                res[i] = rank
            rank += rank_up
        return res


# @lc code=end
