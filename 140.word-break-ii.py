#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # to avoid edge case like 'aaaaaaaaaabaaaa...aaaaa', [a, aa, aaa, ...]
        if not self.canBreak(s, wordDict):
            return
        # bfs
        # queue of index in s
        # use bfs to form a graph
        # use dfs to display all paths
        queue = []
        words = set(wordDict)
        # index to index, directed graph from 0 to len(s)
        graph = defaultdict(set)
        queue.append(0)
        visited = {0}
        # bfs
        while queue:
            start = queue.pop(0)
            # only search forwards
            for end in range(start, len(s) + 1):
                word = s[start:end]
                if word in words:
                    # found a link from start to end, add to graph
                    graph[start].add(end)
                    if end not in visited:
                        queue.append(end)
        # dfs
        sentence = []
        sentences = []
        self.dfs(s, 0, graph, sentence, sentences)
        return sentences

    def dfs(self, s: str, start: int, graph: {int: {int}}, sentence: [str], sentences: List[str]):
        # base case
        if start == len(s):
            sentences.append(' '.join(sentence))
            return

        for end in graph[start]:
            word = s[start:end]
            sentence.append(word)
            self.dfs(s, end, graph, sentence, sentences)
            # backtrack
            sentence.pop()

    def canBreak(self, s: str, wordDict: List[str]) -> bool:
        # bfs
        # queue of index in s
        queue = []
        words = set(wordDict)
        visited = set()
        queue.append(0)
        visited.add(0)
        while queue:
            start = queue.pop(0)
            for end in range(start, len(s) + 1):
                if end in visited:
                    continue
                word = s[start:end]
                if word in words:
                    if end == len(s):
                        return True
                    queue.append(end)
                    visited.add(end)
        return False


s = Solution()
str = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
         aaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaa
         aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
a = s.wordBreak(str, wordDict)
print(a)

str = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
a = s.wordBreak(str, wordDict)
print(a)

str = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
a = s.wordBreak(str, wordDict)
print(a)

# @lc code=end
