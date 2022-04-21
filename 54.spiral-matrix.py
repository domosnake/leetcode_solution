#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # start from (0, 0)
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = 0
        res = [matrix[r][c]]
        matrix[r][c] = -1000
        # direction, start with going left
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 0
        while len(res) != rows * cols:
            r_diff, c_diff = directions[i]
            # add number
            if self._valid_coordinates(matrix, r + r_diff, c + c_diff):
                r += r_diff
                c += c_diff
                res.append(matrix[r][c])
                matrix[r][c] = -1000
            # change direction
            else:
                i = (i + 1) % len(directions)

        return res

    def _valid_coordinates(self, matrix, r, c) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        return (0 <= r < rows) and (0 <= c < cols) and matrix[r][c] >= -100


# s = Solution()
# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# print(s.spiralOrder(a))
# @lc code=end
