#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List


# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        # build graph, bi-directed unweighted graph of all words
        graph = {}
        words.add(beginWord)
        for a in words:
            adjacency = set()
            for b in words:
                # a is connected to b only their diff is 1
                if self.diff(a, b) == 1:
                    adjacency.add(b)
            graph[a] = adjacency

        # we keep storing the predecessor of a given node while doing bfs
        connectTo = {}
        distanceFromBegin = {}
        visited = {}
        for w in words:
            connectTo[w] = None
            distanceFromBegin[w] = float('inf')
            visited[w] = False
        distanceFromBegin[beginWord] = 0

        # bfs
        self.bfs(graph, beginWord, endWord, connectTo, distanceFromBegin, visited)

        # now all our paths can be extracted from connectTo via dfs
        paths = []
        path = []
        self.dfs(beginWord, endWord, connectTo, path, paths)
        
        return paths
    
    def dfs(self, beginWord: str, endWord: str, connectTo: {str: str}, path: List[str], paths: List[List[str]]):
        # base
        if connectTo[beginWord] == endWord: 
            paths.append(path)
            return
    
        # for each connected words 
        for  
    
            // Insert the current 
            // vertex in path 
            path.push_back(u); 
    
            // Recursive call for its parent 
            find_paths(paths, path, parent, 
                    n, par); 
    
            // Remove the current vertex 
        path.pop_back(); 


    def bfs(self, graph: {str: set}, beginWord: str, endWord: str, connectTo: {str: str}, distanceFromBegin: {str: int}, visited: {str: bool}):

        # queue for bfs
        q = [beginWord]

        # bfs
        while q:
            cur = q.pop(0)
            # mark visited
            visited[cur] = True
            # when endWord reached
            if cur == endWord:
                # to find all shortest paths, reset endWords visit flag
                visited[cur] = False
                continue
            # no need to explore longer path
            if distanceFromBegin[cur] >= distanceFromBegin[endWord]:
                # block the way by NOT adding it's adj
                continue
            # explore to adjacent words
            for adj in graph[cur]:
                # update distance
                distanceFromBegin[adj] = distanceFromBegin[cur] + 1
                # update connectTo, cur -> adj
                connectTo[cur] = adj
                # add adj to queue
                q.append(adj)

    def diff(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return -1
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
a = s.findLadders(beginWord, endWord, wordList)
print(a)
# @lc code=end
