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

        # course -> pre
        lookup = defaultdict(set)
        # build graph
        graph = defaultdict(list)
        for p in prerequisites:
            course = p[1]
            pre_course = p[0]
            graph[pre_course].append(course)
            lookup[course].add(pre_course)

        # 0 = not visited, 1 = visited in dfs, -1 = visited outside
        visited = [0] * n
        for c in range(n):
            if visited[c] == -1:
                continue
            self.dfs(c, visited, graph, lookup)
        answer = []
        for pre_course, course in queries:
            answer.append(pre_course in lookup[course])
        return answer

    def dfs(self, cur, visited, graph, lookup):
        # note that we are checking if source -> destination
        if visited[cur] == 1:
            return
        # mark visited for dfs
        visited[cur] = 1
        for next_course in graph[cur]:
            lookup[next_course].update(lookup[cur])
            self.dfs(next_course, visited, graph, lookup)
        # mark visited outside
        visited[cur] = -1

    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # prerequisites[i] = [pre_course, course]
        # queries[i] = [a, b] => is a -> b?

        # this is still a topological sort problem
        # bfs to build prerequisite check table
        graph = defaultdict(list)
        indegree = [0] * n
        # course -> pre, this is KEY
        lookup = defaultdict(set)
        for pre_course, course in prerequisites:
            graph[pre_course].append(course)
            indegree[course] += 1
            lookup[course].add(pre_course)
        queue = [c for c in range(n) if indegree[c] == 0]
        while queue:
            cur = queue.pop(0)
            for next_course in graph[cur]:
                # union
                lookup[next_course].update(lookup[cur])
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        answer = []
        for pre_course, course in queries:
            answer.append(pre_course in lookup[course])
        return answer


# s = Solution()
# a = s.checkIfPrerequisite(
#     5, [[0, 1], [1, 2], [2, 3]],
#     [[0, 4], [4, 0], [1, 3], [3, 0], [0, 1], [2, 0], [1, 4], [3, 1]])
# print(a)
# @lc code=end
