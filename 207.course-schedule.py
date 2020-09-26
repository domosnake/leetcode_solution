#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort - bfs
        # detect a cycle in the directed graph
        # first, build graph as adjacency list
        graph = defaultdict(list)
        # indegree of each vertex
        indegree = [0] * numCourses
        for p in prerequisites:
            course = p[0]
            pre = p[1]
            graph[pre].add(course)
            indegree[course] += 1

        # topological order
        topOrder = []
        # add all nodes with indegree = 0 to queue as starting nodes
        queue = []
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
        # bfs
        while queue:
            course = queue.pop(0)
            topOrder.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    # new start point
                    queue.append(next_course)
        # all couses should be taken
        # if not, there is at least one cycle
        return len(topOrder) == numCourses

    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort - dfs
        # detect a cycle in the directed graph
        # first, build graph as adjacency list
        graph = defaultdict(list)
        for p in prerequisites:
            course = p[0]
            pre = p[1]
            graph[pre].add(course)
        # visited of each vertex
        # 0 = not visited, 1 = visited each dfs, -1 = visited outside
        visited = []
        for c in range(numCourses):
            visited.append(0)
        # topological order
        topOrder = []
        # top sort starting from all vertices one by one
        for c in range(numCourses):
            hasCycle = self.dfs(c, visited, graph, topOrder)
            if hasCycle:
                return False
        return True

    def dfs(self, cur, visited, graph, topOrder) -> bool:
        # when we dfs back to a visited vertex
        # it means there is a cycle
        if visited[cur] == -1:
            return False
        # visited in dfs, hit the end, return True
        if visited[cur] == 1:
            return True
        # mark visited in dfs path
        visited[cur] = 1
        # dfs for all the vertices adjacent to cur
        for next_course in graph[cur]:
            hasCycle = self.dfs(next_course, visited, graph, topOrder)
            if hasCycle:
                return False
        # add top order
        topOrder.append(cur)
        # mark visited in outside
        visited[cur] = -1
        return True


# @lc code=end
