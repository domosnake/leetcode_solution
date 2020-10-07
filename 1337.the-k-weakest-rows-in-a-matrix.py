#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#
from heapq import heappush, heappop
from typing import List


# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        min_heap = []
        for i, row in enumerate(mat):
            soldier = 0
            for n in row:
                if n == 1:
                    soldier += 1
                else:
                    break
            heappush(min_heap, (soldier, i))
        while k > 0:
            res.append(heappop(min_heap)[1])
            k -= 1
        return res


# @lc code=end
