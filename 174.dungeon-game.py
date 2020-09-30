#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
from typing import List


# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return -1
        rows = len(dungeon)
        cols = len(dungeon[0])
        # dp[c] = min_hp_needed
        # we could use dp matrix, but next level only depends prev level
        # space can be optimized from O(rows * cols) to O(cols)
        dp = [float('inf')] * (cols + 1)
        dp[cols - 1] = 1
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                hp_impact = dungeon[r][c]
                # choose min hp needed either from down or right
                min_hp_needed = min(dp[c], dp[c + 1])
                # apply hp impact, see if we can survive
                min_hp_needed = max(min_hp_needed - hp_impact, 1)
                dp[c] = min_hp_needed

        return dp[0]

    def calculateMinimumHP_2d_dp(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return -1
        rows = len(dungeon)
        cols = len(dungeon[0])
        # add some dummy rows and cols to make computation eaiser to write
        dp = [[float('inf') for _ in range(cols + 1)] for _ in range(rows + 1)]
        # init conditions
        dp[rows - 1][cols] = 1
        dp[rows][cols - 1] = 1

        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                hp_impact = dungeon[r][c]
                min_hp_needed = min(dp[r + 1][c], dp[r][c + 1])
                min_hp_needed = max(min_hp_needed - hp_impact, 1)
                dp[r][c] = min_hp_needed

        return dp[0][0]


s = Solution()
d = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
a = s.calculateMinimumHP_2d_dp(d)
print(a)
a = s.calculateMinimumHP(d)
print(a)

# @lc code=end
