#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substrs = []
        self._dfs(s, [], substrs)
        return substrs

    def _dfs(self, s, substr, substrs):
        if not s:
            substrs.append(substr[:])
            return

        for i in range(1, len(s) + 1):
            substr_to_check = s[:i]
            if self._is_palindrome(substr_to_check):
                substr.append(substr_to_check)
                remaining_substr = s[i:]
                self._dfs(remaining_substr, substr, substrs)
                # backtrack
                substr.pop()

    def _is_palindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True


# @lc code=end
