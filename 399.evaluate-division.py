#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from typing import List


# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        # this problem can be considered as a graph problem
        # where letters in equations are nodes
        # values are cost between nodes(directed graph)
        # downstream cost is calculated by multiplication between nodes
        # upstream cost is 1 / downstream
        # e.g. a -> b = 2, b -> c = 3
        # then a -> c = 2 * 3
        # c -> a = 1 / 2 * 3
        #
        # graph vertex -> {vertex: cost}
        graph = {}
        for i in range(len(equations)):
            src = equations[i][0]
            tgt = equations[i][1]
            cost = values[i]
            # add to graph
            # need to add both downstream and upstream
            if src not in graph:
                graph[src] = {tgt: cost}
            else:
                graph[src][tgt] = cost
            if tgt not in graph:
                graph[tgt] = {src: 1 / cost}
            else:
                graph[tgt][src] = 1 / cost
        # solving
        res = []
        for q in queries:
            visited = set()
            start = q[0]
            end = q[1]
            # search start->end and end->start
            res.append(self.dfs(graph, start, end, 1, visited))
        return res

    def dfs(self, graph: dict, start: str, end: str, cost: float, visited: set) -> float:
        # vertex not in graph
        if start not in graph or end not in graph:
            return -1.0
        # edge case start == end
        if start == end:
            return 1.0
        # find the path
        if end in graph[start]:
            return cost * graph[start][end]
        # keep searching
        visited.add(start)
        for connect_to, next_cost in graph[start].items():
            if connect_to not in visited:
                weight = self.dfs(graph, connect_to, end, cost * next_cost, visited)
                # if found path, then return
                if weight != -1.0:
                    return weight
        return -1.0


# @lc code=end
