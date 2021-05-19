#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#


# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 10
        # bfs
        prev = [1] * 10
        cur = [0] * 10
        cur_hops = 1

        while cur_hops <= n - 1:
            cur = [0] * 10
            cur_hops += 1

            for pos in range(10):
                for move in self._moves(pos):
                    cur[pos] += prev[move]
            prev = cur

        return sum(cur) % (10**9 + 7)

    def _moves(self, pos):
        MOVES = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            # no moves starting from 5
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        return MOVES[pos]


# @lc code=end
