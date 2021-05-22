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
        # search in grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # if the cell is land
                if grid[r][c] == '1':
                    # means we find an island
                    islands += 1
                    # search the if surrounding cells are connected to this cell
                    self.dfs(grid, r, c)
        return islands

    def dfs(self, g: List[List[str]], r: int, c: int):
        # beyond boundary
        if r >= len(g) or c >= len(g[0]) or r < 0 or c < 0:
            return
        # dfs to a visited cell, or water
        if g[r][c] != '1':
            return
        # mark visited
        g[r][c] = '$'
        # keep searching 4 directions
        self.dfs(g, r + 1, c)
        self.dfs(g, r - 1, c)
        self.dfs(g, r, c + 1)
        self.dfs(g, r, c - 1)


# @lc code=end
