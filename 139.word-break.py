#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        # dp
        # memo stored whether word s[0:i] can be found at dictionary
        memo = [False] * (len(s) + 1)
        memo[0] = True
        words = set(wordDict)

        for end in range(len(s) + 1):
            for start in range(end):
                prefix = s[start:end]
                if memo[start] and prefix in words:
                    memo[end] = True
                    break
        return memo[-1]


s = Solution()
str = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
a = s.wordBreak(str, wordDict)
print(a)
a = s.wordBreak_dp(str, wordDict)
print(a)

# @lc code=end
