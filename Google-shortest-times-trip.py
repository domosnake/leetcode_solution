# A road trip from city A to city B.
# The time from a city to its connected city takes a unit of time.
# Find the shortest time from city A to city B.
# Input: 1, 3,  [[1, 2], [2, 3]]
# Output: 2
from collections import defaultdict, deque


class Solution:
    def min_time_bfs(self, start, end, string):
        g = self._buildGraph(string)
        visited = set()
        min_time = float('inf')
        times = 0
        q = deque()
        q.append(start)
        visited.add(start)

        while q:
            cur = q.popleft()

            # bfs, once we find min, it is the shortest time
            if cur == end:
                min_time = min(min_time, times)
                break

            for child in g[cur]:
                if child not in visited:
                    q.append(child)
                    visited.add(child)
            times += 1

        return min_time

    def min_time_dfs(self, start, end, string):
        g = self._buildGraph(string)
        visited = set()
        min_time = [float('inf')]

        self._dfs(start, end, g, visited, 0, min_time)
        return min_time[0]

    def _dfs(self, start, end, g, visited, times, min_time):
        if start == end:
            min_time[0] = min(times, min_time[0])
            return

        if start in visited:
            return

        visited.add(start)
        for child in g[start]:
            self._dfs(child, end, g, visited, times + 1, min_time)

    def _buildGraph(self, string):
        g = defaultdict(list)
        for p in string:
            # start to end
            g[p[0]].append(p[1])
            # end to start
            g[p[1]].append(p[0])
        return g


s = Solution()
a = s.min_time_bfs(1, 4, [[1, 2], [2, 3], [1, 3], [3, 4]])
print(a)
