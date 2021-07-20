#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # row, col, removed obstacles, step
        q = deque()
        q.append((0, 0, k, 0))
        visited = set()
        visited.add((0, 0, k))
        # edge case
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0

        while q:
            row, col, K, step = q.popleft()
            # go 4 directions
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                # whihin bound and not visited
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c] == 1 and K > 0 and (r, c, K - 1) not in visited:
                        visited.add((r, c, K - 1))
                        q.append((r, c, K - 1, step + 1))
                    if grid[r][c] == 0 and (r, c, K) not in visited:
                        # reach end
                        if r == len(grid) - 1 and c == len(grid[0]) - 1:
                            return step + 1
                        visited.add((r, c, K))
                        q.append((r, c, K, step + 1))
        # unreachable end
        return -1


# @lc code=end
