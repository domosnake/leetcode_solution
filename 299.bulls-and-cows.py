#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
from collections import Counter


# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 2 item counters
        s = Counter(secret)
        g = Counter(guess)
        # intersection is cows
        b = sum((s & g).values())
        a = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
        # some cows are actually bulls
        b -= a
        return f'{a}A{b}B'


# @lc code=end
