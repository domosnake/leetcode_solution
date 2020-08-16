# You have a map that marks the locations of treasure islands.
# Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in.
# There are other explorers trying to find the treasure.
# So you must figure out a shortest route to one of the treasure islands.
#
# Assume the map area is a two dimensional grid, represented by a matrix of characters.
# You must start from one of the starting points (marked as S) and can move one block up, down, left or right at a time.
# The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D.
# You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
# Output the minimum number of steps to get to any of the treasure islands.
#
# Example:

# Input:
# [['S', 'O', 'O', 'S', 'S'],
#  ['D', 'O', 'D', 'O', 'D'],
#  ['O', 'O', 'O', 'O', 'X'],
#  ['X', 'D', 'D', 'O', 'O'],
#  ['X', 'D', 'D', 'D', 'O']]
#
# Output: 3
# Explanation:
# You can start from (0,0), (0, 3) or (0, 4).
# The treasure locations are (2, 4) (3, 0) and (4, 0).
# Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

from typing import List


class Solution:
    def shortestPathToTreasureIsland_bfs(self, grid: List[List[str]]) -> int:
        # bfs from start point to X, mark searched cell as 'S'
        # start point
        queue = []
        queue_temp = []
        steps = 0
        # store all starting points
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    queue.append((i, j))

        # keep searching until all water is explored or one of the X is found
        while True:
            steps += 1
            while queue:
                cur_pos = queue.pop(0)
                i = cur_pos[0]
                j = cur_pos[1]
                # mark the cell visited and continue seaching
                grid[i][j] = 'V'
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


s = Solution()
grid = [['S', 'O', 'O', 'S', 'S'],
        ['D', 'O', 'D', 'O', 'D'],
        ['O', 'O', 'O', 'O', 'X'],
        ['X', 'D', 'D', 'O', 'O'],
        ['X', 'D', 'D', 'D', 'O']]
a = s.shortestPathToTreasureIsland_bfs(grid)
print(a)
