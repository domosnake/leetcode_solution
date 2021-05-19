# Imagine you place a knight chess piece on a phone dial pad.
# This chess piece moves in an uppercase “L” shape.

# Suppose you dial keys on the keypad using only hops a knight can make.
# Every time the knight lands on a key, we dial that key and make another hop.
# The starting position counts as being dialed.

# How many distinct numbers can you dial in N hops from a particular starting position?


class Solution:
    def countPaths_bfs_memo(self, start_pos, hops):
        prev = [1] * 10
        cur = [0] * 10
        cur_hops = 1

        while cur_hops <= hops:
            cur = [0] * 10
            cur_hops += 1

            for pos in range(10):
                for move in self._moves(pos):
                    cur[pos] += prev[move]
            prev = cur

        return cur[start_pos]

    def countPaths_dfs_cache(self, start_pos, hops):
        cache = {}
        paths = self._dfs(cache, start_pos, hops)
        return paths

    def _dfs(self, cache, start_pos, hops):
        # use cache
        if (start_pos, hops) in cache:
            return cache[(start_pos, hops)]

        if hops == 0:
            return 1

        paths = 0
        for pos in self._moves(start_pos):
            paths += self._dfs(cache, pos, hops - 1)
        # save cache
        cache[start_pos, hops] = paths
        return paths

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


s = Solution()
a = s.countPaths_bfs_memo(1, 3)
print(a)
