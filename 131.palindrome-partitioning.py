#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self._dfs(s, [], res)
        return res

    def _dfs(self, s, path, res):
        if not s:
            res.append(path[:])
            return

        for i in range(1, len(s) + 1):
            if self._isPal(s[:i]):
                path.append(s[:i])
                self._dfs(s[i:], path, res)
                # backtrack
                path.pop()

    def _isPal(self, s):
        return s == s[::-1]


# @lc code=end
