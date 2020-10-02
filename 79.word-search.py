#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        # dfs at each cell
        for r in range(len(board)):
            for c in range(len(board[0])):
                # dfs
                if self.dfs(word, 0, board, r, c):
                    return True
        return False

    def dfs(self, word, at, board, r, c) -> bool:
        # beyong bounds
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return False
        # visited
        if board[r][c] == '$':
            return False
        # not match
        if board[r][c] != word[at]:
            return False
        # all char match
        if at == len(word) - 1 and board[r][c] == word[at]:
            return True

        # mark visited
        board[r][c] = '$'
        # dfs 4 directions
        if self.dfs(word, at + 1, board, r, c - 1):
            return True
        if self.dfs(word, at + 1, board, r, c + 1):
            return True
        if self.dfs(word, at + 1, board, r - 1, c):
            return True
        if self.dfs(word, at + 1, board, r + 1, c):
            return True
        # back track
        board[r][c] = word[at]

        return False


# @lc code=end
