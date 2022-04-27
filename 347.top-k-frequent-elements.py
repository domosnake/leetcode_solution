#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use min_heap (size = k) to find top k max
        min_heap = []
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for n, freq in counter.items():
            heappush(min_heap, (freq, n))
            if len(min_heap) > k:
                heappop(min_heap)
        return [item[1] for item in min_heap]


# s = Solution()
# a = s.topKFrequent([1, 1, 1, 2, 3, 2, 3, 4, 5], 3)
# print(a)
# @lc code=end
