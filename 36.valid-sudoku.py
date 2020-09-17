#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

from typing import List


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # check rows
        for row in board:
            if not self.isValidGrid(row):
                return False
        # check cols
        for i in range(n):
            col = [row[i] for row in board]
            if not self.isValidGrid(col):
                return False
        # check boxes
        # start positions of boxes:
        # (0, 0), (0, 3), (0, 6)
        # (3, 0), (3, 3), (3, 6)
        # (6, 0), (6, 3), (6, 6)
        BOX_LEN = 3
        for r in range(0, n, BOX_LEN):
            for c in range(0, n, BOX_LEN):
                box = []
                # get a box
                for i in range(r, r + BOX_LEN):
                    for j in range(c, c + BOX_LEN):
                        box.append(board[i][j])
                # validate
                if not self.isValidGrid(box):
                    return False
        return True

    # check if a grid in a sudoku is valid
    # a grid can be a row/col/box in a sodoku
    def isValidGrid(self, grid: List[str]) -> bool:
        digits = set()
        for cell in grid:
            if cell != '.':
                if cell in digits:
                    return False
                else:
                    digits.add(cell)
        return True


s = Solution()
m = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
     [".", ".", ".", "5", "6", ".", ".", ".", "."],
     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
     [".", ".", ".", "7", ".", ".", ".", ".", "."],
     [".", ".", ".", "4", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "2", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "2"]]
a = s.isValidSudoku(m)
print(a)

# @lc code=end
