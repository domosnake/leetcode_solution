#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
#
from string import ascii_lowercase


# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        backwards = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                backwards += ascii_lowercase[int(s[i - 2: i]) - 1]
                i -= 3
            else:
                backwards += ascii_lowercase[int(s[i]) - 1]
                i -= 1
        return backwards[::-1]


# @lc code=end
