#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
from typing import List
from heapq import heappop, heappush
from math import sqrt


# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K <= 0:
            return []
        if K >= len(points):
            return points
        # top k
        # min heap
        minHeap = []
        for p in points:
            distance = sqrt(p[0] * p[0] + p[1] * p[1])
            heappush(minHeap, (distance, p))

        res = []
        for _ in range(K):
            res.append(heappop(minHeap)[1])
        return res


# @lc code=end
