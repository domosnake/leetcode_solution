#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest_max_heap(self, matrix: List[List[int]], k: int) -> int:
        # max heap
        max_heap = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heappush(max_heap, -matrix[r][c])
                if len(max_heap) > k:
                    heappop(max_heap)
        return -max_heap[0]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # min heap for each row
        min_heap = []
        row = len(matrix)
        col = len(matrix[0])
        for r in range(min(k, row)):
            heappush(min_heap, (matrix[r][0], r, 0))
        for _ in range(k):
            val, r, c = heappop(min_heap)
            # check range
            if c + 1 < col:
                heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        return val

# @lc code=end
