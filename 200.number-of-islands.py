#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        # build matrix
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if the cell is land
                if grid[row][col] == '1':
                    # means we find an island
                    islands += 1
                    # search the if surrounding  cells are connected to this cell
                    self.dfs(row, col, grid)
        return islands

    def dfs(self, r: int, c: int, matrix: List[List[str]]):
        # beyond boundary
        if r >= len(matrix) or c >= len(matrix[0]) or r < 0 or c < 0:
            return
        # dfs to a visited cell， or water
        if matrix[r][c] == '$' or matrix[r][c] == '0':
            return
        # mark visited
        matrix[r][c] = '$'
        # keep searching 4 directions
        self.dfs(r + 1, c, matrix)
        self.dfs(r - 1, c, matrix)
        self.dfs(r, c + 1, matrix)
        self.dfs(r, c - 1, matrix)


# @lc code=end
