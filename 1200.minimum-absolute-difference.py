#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#
from typing import List


# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        asc = sorted(arr)
        min_dis = float('inf')
        res = []
        for i in range(1, len(asc)):
            dis = asc[i] - asc[i - 1]
            if dis < min_dis:
                min_dis = dis
                res.clear()
                res.append(asc[i - 1: i + 1])
            elif dis == min_dis:
                res.append(asc[i - 1: i + 1])

        return res


# @lc code=end
