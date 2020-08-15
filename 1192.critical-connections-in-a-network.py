#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
from typing import List, Set
from collections import defaultdict


# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        # build graph:
        for src, des in connections:
            graph[src].append(des)
            graph[des].append(src)

        # discovery time of nodes from starting node
        time = 0
        # discovery time of nodes
        discTime = {}
        # lowest discovery time of nodes
        lowTime = {}
        # store parent of nodes, default to -1
        parent = dict.fromkeys(range(n))
        visited = set()
        result = []

        # loop thru all nodes
        # note that the graph may contain multiple connected components
        # thus, we are trying to dfs startig from each unvisited node
        for node in graph:
            if node not in visited:
                self.dfs_AE(graph, discTime, lowTime, visited, time, node, parent, result)
        return result

    def dfs_AE(self, graph: {}, discTime: {}, lowTime: {}, visited: Set[int], time: int, node: int, parent: {}, result: [int]):
        # mark visited
        visited.add(node)
        # init discovery and low time for cur node
        discTime[node] = time
        lowTime[node] = time
        # increament time
        time += 1
        # searching all nodes connected to cur node
        for nextNode in graph[node]:
            # avoid searching back to parent and only search the non-parent adjacent nodes
            if parent[node] == nextNode:
                continue

            # if not visited
            if nextNode not in visited:
                # cur node is the parent of the nextNode
                parent[nextNode] = node
                # keep dfs searching
                self.dfs_AE(graph, discTime, lowTime, visited, time, nextNode, parent, result)

            # when cur node gets updated with lower time, this means there is a cycle or back edge
            lowTime[node] = min(lowTime[node], lowTime[nextNode])

            # AE CONDITION:
            # low time(child node) > discovery time(parnet node)
            if lowTime[nextNode] > discTime[node]:
                result.append([node, nextNode])


# @lc code=end
