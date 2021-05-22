#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare_space_mn(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        # max side for each cell in dp
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        max_side = 0

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    dp[r + 1][c + 1] = 1
                    dp[r][c] += min(dp[r][c + 1], dp[r][c], dp[r + 1][c])
                    max_side = max(dp[r + 1][c + 1], max_side)

        return max_side**2

    # space optimized
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        # note that we only need dp[r-1][c], dp[r-1][c-1], dp[r][c-1]
        # thus 1 row and 1 front
        dp_row = [0] * (col + 1)
        front = 0
        max_side = 0

        for r in range(row):
            next_dp_row = []
            for c in range(col):
                cur = 0
                if matrix[r][c] == '1':
                    cur = 1
                    cur += min(dp_row[c], dp_row[c + 1], front)
                    max_side = max(cur, max_side)
                # update front
                front = cur
                # update next dp row
                next_dp_row.append(cur)
            # update dp and front
            front = 0
            dp_row = [front] + next_dp_row

        return max_side**2


# @lc code=end
