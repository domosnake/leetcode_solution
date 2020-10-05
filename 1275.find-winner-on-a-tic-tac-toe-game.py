#
# @lc app=leetcode id=1275 lang=python3
#
# [1275] Find Winner on a Tic Tac Toe Game
#
from typing import List


# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # A will play first
        if not moves:
            return 'Pending'
        game = [[' '] * 3 for _ in range(3)]
        for i, m in enumerate(moves):
            game[m[0]][m[1]] = 'X' if i % 2 == 0 else 'O'
        # check game
        for row in game:
            if row[0] == row[1] == row[2] == 'X':
                return 'A'
            elif row[0] == row[1] == row[2] == 'O':
                return 'B'

        for c in range(3):
            if game[0][c] == game[1][c] == game[2][c] == 'X':
                return 'A'
            elif game[0][c] == game[1][c] == game[2][c] == 'O':
                return 'B'

        if game[0][0] == game[1][1] == game[2][2] == 'X':
            return 'A'
        if game[0][2] == game[1][1] == game[2][0] == 'X':
            return 'A'
        if game[0][0] == game[1][1] == game[2][2] == 'O':
            return 'B'
        if game[0][2] == game[1][1] == game[2][0] == 'O':
            return 'B'

        if len(moves) == 9:
            return 'Draw'
        return 'Pending'


# @lc code=end
