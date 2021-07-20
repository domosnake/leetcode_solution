from typing import List
from collections import deque


class Solution:
    def shortestPath(self, matrix: List[List[str]], remove: int = 0) -> int:
        start = None
        end = None
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 'S':
                    start = (r, c)
                if matrix[r][c] == 'E':
                    end = (r, c)

        # start and end must be in matrix
        if not start or not end:
            return -1
        # row, col, remove, step
        q = deque()
        q.append((start[0], start[1], remove, 0))
        visited = set()
        visited.add((start[0], start[1], remove))
        while q:
            _r, _c, k, step = q.popleft()
            # go 4 directions
            for r, c in [(_r + 1, _c), (_r - 1, _c), (_r, _c + 1), (_r, _c - 1)]:
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                    if matrix[r][c] == '1' and k > 0 and (r, c, k - 1) not in visited:
                        q.append((r, c, k - 1, step + 1))
                        visited.add((r, c, k - 1))
                    if matrix[r][c] == '0' and (r, c, k) not in visited:
                        q.append((r, c, k, step + 1))
                        visited.add((r, c, k))
                    if matrix[r][c] == 'E':
                        return step + 1

        return -1


s = Solution()
a = [['S', '1', '1'],
     ['1', '1', '1'],
     ['1', '0', 'E']]

b = [['S', '0', '0'],
     ['1', '1', '0'],
     ['1', '1', '0'],
     ['1', 'E', '1'],
     ['0', '0', '1']]

c = s.shortestPath(a)
print(c)
c = s.shortestPath(a, 2)
print(c)
c = s.shortestPath(b, 1)
print(c)
c = s.shortestPath(b, 2)
print(c)
