# Find thr word in a matrix of letters.
# We can only go horizontally or vertically one cell in the matrix.
# Return true if we can form the word in the matrix, false otherwise.
#
# [
#   ['a', 'b', 'c'],
#   ['x', 'e', 't'],
#   ['y', 't', 'c'],
#   ['a', 'b', 'c']
# ]
# target = abc, return True
# target = bet, return True
# target = xyz, return False
from typing import List


class Solution:
    def findWord(self, matrix: List[List[str]], target: str) -> bool:
        if not matrix:
            return False
        if not target:
            return True

        startCells = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target[0]:
                    startCells.append((r, c))

        if not startCells:
            return False
        for cell in startCells:
            if self.dfs(matrix, target, 0, cell[0], cell[1]):
                return True
        return False

    def dfs(self, matrix: List[List[str]], target: str, i: int, r: int, c: int) -> bool:
        if i == len(target):
            return True
        if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
            return False
        if matrix == '$':
            return False
        if target[i] != matrix[r][c]:
            return False
        # mark visited
        temp = matrix[r][c]
        matrix[r][c] = '$'
        i += 1

        down = self.dfs(matrix, target, i, r+1, c)
        up = self.dfs(matrix, target, i, r-1, c)
        right = self.dfs(matrix, target, i, r, c+1)
        left = self.dfs(matrix, target, i, r, c-1)
        found = up or down or right or left

        # backtrack, unmark visited
        matrix[r][c] = temp
        i -= 1
        return found


s = Solution()
m = [
        ['a', 'b', 'c'],
        ['x', 'e', 't'],
        ['y', 'p', 'c'],
        ['a', 'b', 'c']
    ]
a = s.findWord(m, 'bet')
print(a)
a = s.findWord(m, 'xyz')
print(a)
