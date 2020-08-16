#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
from typing import List


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # naive sort and find h index, with O(nlogn) time
        # we cannot change the definition of h-index
        # improve sorting time, use bucket sort with O(n) time
        # build a bucket of size n + 1 to hold citation count, why n + 1
        # first nth to hold count <= n, n+1th to hold count > n
        n = len(citations)
        bucket = [0]*(n+1)
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1
        # definition of h-index
        count = 0
        for i in range(n, -1, -1):
            count += bucket[i]
            if count >= i:
                return i
        return 0


# @lc code=end
