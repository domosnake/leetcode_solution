#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # only mid nodes can be the root of Minimum Height Trees
        # we can keep removing leaves and related edges till we reach 1 or 2
        if not edges:
            return [i for i in range(n)]
        # build graph
        graph = defaultdict(set)
        for p, q in edges:
            graph[p].add(q)
            graph[q].add(p)

        leaves = [node for node in graph if len(graph[node]) == 1]
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves

    def findMinHeightTrees_longest_path(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [i for i in range(n)]
        # build graph
        graph = defaultdict(set)
        for p, q in edges:
            graph[p].add(q)
            graph[q].add(p)

        # pick a node randomly, find it's longest path
        # then pick the farest node(last) in that path
        # and dfs again to find the longest path of the tree
        # min height trees have to choose mid node(s) as the root
        # dfs to find the longest path in a tree
        longest = self.dfs(graph, 0, set(), [], [])
        longest = self.dfs(graph, longest[-1], set(), [], [])

        mid = len(longest) // 2
        if len(longest) % 2 == 0:
            return [longest[mid], longest[mid - 1]]
        else:
            return [longest[mid]]

    def dfs(self, graph, node, visited, path, longest):
        if node in visited:
            if len(path) > len(longest):
                longest.clear()
                longest.extend(path.copy())
            return longest
        path.append(node)
        visited.add(node)
        for child in graph[node]:
            self.dfs(graph, child, visited, path, longest)
        path.pop()
        return longest


# s = Solution()
# a = s.findMinHeightTrees(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]])
# print(a)

# @lc code=end
