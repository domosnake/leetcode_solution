#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#


# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        at = (0, 0)
        visited = {at}
        for move in path:
            if move == 'N':
                at = (at[0], at[1] + 1)
            elif move == 'S':
                at = (at[0], at[1] - 1)
            elif move == 'E':
                at = (at[0] + 1, at[1])
            elif move == 'W':
                at = (at[0] - 1, at[1])
            else:
                continue
            if at in visited:
                return True
            visited.add(at)
        return False


# @lc code=end
