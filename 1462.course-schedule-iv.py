#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def checkIfPrerequisite_dfs(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prerequisites[i] = [pre_course, course]
        # queries[i] = [a, b] => is a -> b?

        # this is still a topological sort problem
        # dfs to build prerequisite check table

        lookup = defaultdict(set)
        # build graph
        graph = defaultdict(list)
        for p in prerequisites:
            course = p[1]
            pre_course = p[0]
            graph[pre_course].append(course)
            lookup[pre_course].add(course)

        # 0 = not visited, 1 = visited in dfs, -1 = visited outside
        visited = [0] * n
        for c in range(n):
            # tree pruning
            if visited[c] == -1:
                continue
            self.dfs(c, visited, graph)

        return answer

    def dfs(self, cur, visited, graph) -> bool:
        # note that we are checking if source -> destination
        if visited[cur] == 1:
            return
        visited[cur] = 1
        for next_course in graph[src]:
            # found answer, early return
            if self.dfs(next_course, des, visited, graph):
                return True
        # dfs all node, source and destination has no relation
        return False


# s = Solution()
# a = s.checkIfPrerequisite(5, [[3, 4], [2, 3], [1, 2], [0, 1]],
#                           [[0, 4], [4, 0], [1, 3], [3, 0]])
# print(a)
# @lc code=end
