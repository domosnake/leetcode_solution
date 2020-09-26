#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def findOrder_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prerequisites[i] = [course, pre_course]
        # find one topological order if any
        # note that a DAG can have multiple top orders
        # DFS

        # build graph
        graph = defaultdict(list)
        for p in prerequisites:
            pre_course = p[1]
            course = p[0]
            graph[pre_course].append(course)

        # 0 = not visited, 1 = visited in dfs, -1 = visited outside
        visited = [0] * numCourses
        topOrder = []
        for c in range(numCourses):
            # cycle, early return
            if not self.dfs(c, visited, graph, topOrder):
                return []
        # top order should be reversed due to stack(dfs)
        return topOrder[::-1]

    def dfs(self, cur, visited, graph, topOrder) -> bool:
        # tree pruning
        if visited[cur] == -1:
            return True
        # cycle
        if visited[cur] == 1:
            return False

        # mark visited in dfs
        visited[cur] = 1
        for next_course in graph[cur]:
            # cycle, early return
            if not self.dfs(next_course, visited, graph, topOrder):
                return False

        # mark visited outside
        visited[cur] = -1
        # add top order
        topOrder.append(cur)
        return True

    def findOrder_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prerequisites[i] = [course, pre_course]
        # find one topological order if any
        # note that a DAG can have multiple top orders
        # BFS

        # build graph
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for p in prerequisites:
            pre_course = p[1]
            course = p[0]
            graph[pre_course].append(course)
            indegree[course] += 1

        topOrder = []
        queue = []
        for c in range(numCourses):
            # add all 0 indgree to queue
            if indegree[c] == 0:
                queue.append(c)
        # bfs
        while queue:
            cur = queue.pop(0)
            # add to top order
            topOrder.append(cur)
            # bfs all next_course
            for next_course in graph[cur]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    # next starting point
                    queue.append(next_course)
                # early cycle detection
                elif indegree[next_course] < 0:
                    return []
        # when ends, if topOrder doesn't has the same size as numCourses
        # then there is a least a cycle, and we can not take all courses
        return topOrder


# s = Solution()
# a = s.findOrder(2, [[1, 0]])
# print(a)


# @lc code=end
