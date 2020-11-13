#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#
from typing import List


# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # dfs
        if not board or len(board[0]) < 1:
            return 0
        ships = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    ships += 1
                    self.dfs(board, r, c)
        return ships

    def dfs(self, board, r, c):
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return
        if board[r][c] != 'X':
            return
        board[r][c] = '$'
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)


# @lc code=end
