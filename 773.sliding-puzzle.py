#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
from typing import List


# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        cols = len(board[0])
        # to find the min distance from a node to a node
        target = '123450'

        # bfs
        cur = ''.join(str(d) for r in board for d in r)
        visited = {cur}
        queue = [(cur, cur.index('0'))]
        moves = 0

        while queue:
            next_queue = []
            # process all nodes at current level
            for cur, i in queue:
                visited.add(cur)
                if cur == target:
                    return moves

                # up, down, left, right
                swap = []
                if 0 <= i - cols < len(target):
                    swap.append(i - cols)
                if 0 <= i + cols < len(target):
                    swap.append(i + cols)
                if 0 <= i % cols - 1 < cols:
                    swap.append(i - 1)
                if 0 <= i % cols + 1 < cols:
                    swap.append(i + 1)

                for j in swap:
                    chars = [d for d in cur]
                    chars[i], chars[j] = chars[j], chars[i]
                    new_cur = ''.join(chars)
                    if new_cur not in visited:
                        next_queue.append((new_cur, j))
            moves += 1
            queue = next_queue

        return -1


# s = Solution()
# b = [[1,2,3],[4,0,5]]
# a = s.slidingPuzzle(b)
# print(a)

# @lc code=end
