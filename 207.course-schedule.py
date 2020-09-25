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
        # first, build graph as adjacency matrix
        graph = defaultdict(set)
        # indegree of each vertex
        indegree = [0] * numCourses
        # topological order
        topOrder = []
        for p in prerequisites:
            course = p[0]
            pre = p[1]
            graph[pre].add(course)
            indegree[course] += 1
        # add all nodes with indegree = 0 to queue as starting nodes
        queue = []
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)

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


# @lc code=end
