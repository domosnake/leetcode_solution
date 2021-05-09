#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
from typing import List


# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        # replace same color with new color by dfs
        self._dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def _dfs(self, image, r, c, oldColor, newColor):
        if 0 > r or r >= len(image) or 0 > c or c >= len(image[0]):
            return
        if image[r][c] != oldColor:
            return
        if image[r][c] == newColor:
            return

        image[r][c] = newColor
        self._dfs(image, r + 1, c, oldColor, newColor)
        self._dfs(image, r - 1, c, oldColor, newColor)
        self._dfs(image, r, c + 1, oldColor, newColor)
        self._dfs(image, r, c - 1, oldColor, newColor)


# @lc code=end
