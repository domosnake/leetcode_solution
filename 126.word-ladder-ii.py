#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        # bi-directed graph of all words
        graph = {}
        words.add(beginWord)
        for a in words:
            adjacency = set()
            for b in words:
                # a is connected to b only their diff is 1
                if self.diff(a, b) == 1:
                    adjacency.add(b)
            graph[a] = adjacency

        # dfs all path(s) from begin to end
        paths = []
        path = [beginWord]
        visited = set()
        self.dfs(graph, paths, path, visited, endWord)
        if not paths:
            return []

        # pop shortest paths from heap
        shortest = paths[0][0]
        shortestPaths = []
        while paths:
            p = heappop(paths)
            if p[0] > shortest:
                break
            shortestPaths.append(p[1])

        return shortestPaths

    def dfs(self, graph: {}, paths: [], path: [], visited: set, endWord: str):
        # base
        if path[-1] == endWord:
            # save copied path, len is the key
            heappush(paths, (len(path), path[:]))
            return

        # mark visited
        visited.add(path[-1])
        # keep dfs for each adjacent word
        for word in graph[path[-1]]:
            if word in visited:
                continue
            path.append(word)
            # keep searching next word
            self.dfs(graph, paths, path, visited, endWord)
            # backtrack and unmark visited
            path.pop()
            visited.discard(word)

    def diff(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return -1
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff


# s = Solution()
# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog","dot"]
# a = s.findLadders(beginWord, endWord, wordList)
# print(a)
# @lc code=end
