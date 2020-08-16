# You have a map that marks the location of a treasure island.
# Some of the map area has jagged rocks and dangerous reefs.
# Other areas are safe to sail in. There are other explorers trying to find the treasure.
# So you must figure out a shortest route to the treasure island.
#
# Assume the map area is a two dimensional grid, represented by a matrix of characters.
# You must start from the top-left corner of the map and can move one block up, down, left or right at a time.
# The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner.
# Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
# You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe.
# Output the minimum number of steps to get to the treasure.
#
# Example:
#
# Input:
# [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]
#
# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

from typing import List


class Solution:
    def shortestPathToTreasureIsland_bfs(self, grid: List[List[str]]) -> int:
        # bfs from start point to X, mark searched cell as 'S'
        # start point
        queue = [(0, 0)]
        queue_temp = []
        steps = 0
        # keep searching until all water is explored
        while True:
            steps += 1
            while queue:
                cur_pos = queue.pop(0)
                i = cur_pos[0]
                j = cur_pos[1]
                # mark the cell searched and continue seaching
                grid[i][j] = 'S'
                for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        # find the treasure
                        if grid[r][c] == 'X':
                            return steps
                        # only search unvisited open water
                        if grid[r][c] == 'O':
                            queue_temp.append((r, c))
            # swap queues
            queue = queue_temp
            queue_temp = []
            if not queue:
                break
        # search the map, no treasure island
        return -1

    def shortestPathToTreasureIsland_dfs(self, grid: List[List[str]]) -> int:
        steps = self.dfs(grid, 0, 0, 0)
        # this means it will never find treasure
        if steps == float('inf'):
            return -1
        return steps

    def dfs(self, grid: List[List[str]], r: int, c: int, curSteps: int) -> int:
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return float('inf')
        if grid[r][c] == 'S' or grid[r][c] == 'D':
            return float('inf')
        if grid[r][c] == 'X':
            return curSteps
        # mark searched
        grid[r][c] = 'S'

        # search 4 directions
        up = self.dfs(grid, r - 1, c, curSteps + 1)
        down = self.dfs(grid, r + 1, c, curSteps + 1)
        left = self.dfs(grid, r, c - 1, curSteps + 1)
        right = self.dfs(grid, r, c + 1, curSteps + 1)
        # backtrack
        grid[r][c] = 'O'
        # return shorest
        return min(up, down, left, right)


s = Solution()
grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]
a = s.shortestPathToTreasureIsland_bfs(grid)
print(a)

grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['D', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]
a = s.shortestPathToTreasureIsland_bfs(grid)
print(a)

grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]
a = s.shortestPathToTreasureIsland_dfs(grid)
print(a)

grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['D', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]
a = s.shortestPathToTreasureIsland_dfs(grid)
print(a)
