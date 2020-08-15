#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
from typing import List


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citation is sorted in ascending order
        # bi-search the mid
        if not citations:
            return 0
        return self.binary_search(citations, 0, len(citations) - 1)

    def binary_search(self, citations: List[int], start: int, end: int) -> int:
        # base, stop here
        # start points to 1 unit left to h or 1 unit right to h
        if start > end:
            return len(citations) - start

        mid = (start + end) // 2
        # index in descending order, starting at 1
        index = len(citations) - mid
        # if mid > index, search left half
        if citations[mid] > index:
            return self.binary_search(citations, start, mid - 1)
        # if mid < index, search right half
        elif citations[mid] < index:
            return self.binary_search(citations, mid + 1, end)
        # if mid == index, return h
        else:
            return index


# @lc code=end
