from typing import List, Set
from collections import defaultdict

# You are given an undirected connected graph.
# An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges,
# makes the graph disconnected (or more precisely, increases the number of connected components in the graph).
# The task is to find all articulation points in the given graph.
#
# Input:
# The input to the function/method consists of three arguments:
#
# numNodes, an integer representing the number of nodes in the graph.
# numEdges, an integer representing the number of edges in the graph.
# edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
# Output:
# Return a list of integers representing the critical nodes.


class Solution:
    # articulation points
    def findAP(self, v: int, e: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        # build graph:
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        # discovery time of nodes from starting node
        time = 0
        # discovery time of nodes
        discTime = {}
        # lowest discovery time of nodes
        lowTime = {}
        # store parent of nodes, default to -1
        parent = dict.fromkeys(range(v))
        visited = set()
        result = []

        # loop thru all nodes
        # note that the graph may contain multiple connected components
        # thus, we are trying to dfs startig from each unvisited node
        for node in graph:
            if node not in visited:
                self.dfs_AP(graph, discTime, lowTime, visited, time, node, parent, result)
        return result

    def dfs_AP(self, graph: {}, discTime: {}, lowTime: {}, visited: Set[int], time: int, node: int, parent: {}, result: [int]):
        # mark visited
        visited.add(node)
        # init discovery and low time for cur node
        discTime[node] = time
        lowTime[node] = time
        # increament time
        time += 1

        # children count of cur node in dfs spanning tree
        children = 0

        # searching all nodes connected to cur node
        for nextNode in graph[node]:
            # avoid searching back to parent and only search the non-parent adjacent nodes
            if parent[node] == nextNode:
                continue

            # if not visited
            if nextNode not in visited:
                children += 1
                # cur node is the parent of the nextNode
                parent[nextNode] = node
                # keep dfs searching
                self.dfs_AP(graph, discTime, lowTime, visited, time, nextNode, parent, result)

            # when cur node gets updated with lower time, this usually means there is a cycle
            lowTime[node] = min(lowTime[node], lowTime[nextNode])

            # AP CONDITIONS:
            # in dfs spanning tree, if one of below conditions meets, the cur/parent node is an AP
            # (1) if node is root, it has at least 2 children
            # (2) for any other nodes, low time(child node) >= discovery time(parnet node), then the cur/parent node is an AP
            # root
            if parent[node] is None:
                if children > 2:
                    result.append[node]
            # any other nodes
            else:
                if lowTime[nextNode] >= discTime[node]:
                    result.append(node)

    # articulation edges
    def findAE(self, v: int, e: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        # build graph:
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)

        # discovery time of nodes from starting node
        time = 0
        # discovery time of nodes
        discTime = {}
        # lowest discovery time of nodes
        lowTime = {}
        # store parent of nodes, default to -1
        parent = dict.fromkeys(range(v))
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


s = Solution()

numNodes = 10
numEdges = 9
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4], [7, 8],
         [8, 9]]
a = s.findAE(numNodes, numEdges, edges)
print(a)

a = s.findAP(numNodes, numEdges, edges)
print(a)
