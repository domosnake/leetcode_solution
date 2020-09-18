#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List
# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #  clockwise by 90 degree
        #  first reverse rows
        #  then transpose
        #  1 2 3     7 8 9     7 4 1
        #  4 5 6  => 4 5 6  => 8 5 2
        #  7 8 9     1 2 3     9 6 3
        #  counter-clockwise by 90 degree
        #  first transpose
        #  then reverse rows
        #  1 2 3     1 4 7     3 6 9
        #  4 5 6  => 2 5 8  => 2 5 8
        #  7 8 9     3 6 9     1 4 7
        CLOCKWISE = True
        if CLOCKWISE:
            self.reverseRows(matrix)
            self.transposeMatrix(matrix)
        else:
            self.transposeMatrix(matrix)
            self.reverseRows(matrix)

    def reverseRows(self, matrix: List[List[int]]):
        # for each col
        for c in range(len(matrix)):
            lo = 0
            hi = len(matrix) - 1
            while lo < hi:
                # swap
                matrix[lo][c], matrix[hi][c] = matrix[hi][c], matrix[lo][c]
                lo += 1
                hi -= 1

    def transposeMatrix(self, matrix: List[List[int]]):
        # swap cells at [r, c] and [c, r]
        # [1, 3] <=> [3, 1]
        # thus transpose
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


# @lc code=end
