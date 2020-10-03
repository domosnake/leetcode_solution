#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#
from typing import List


# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str],
                              words: List[str]) -> List[int]:
        # each answer[i] is the number of words
        # such that f(queries[i]) < f(W)
        # where f(s) is a function that
        # calculates the frequency of the smallest character in s
        # for example: s = "dcce" then f(s) = 2
        q_count = []
        w_count = []
        res = []
        for q in queries:
            q_count.append(self.minCharFreq(q))
        for w in words:
            w_count.append(self.minCharFreq(w))

        for qc in q_count:
            ans = 0
            for wc in w_count:
                if qc < wc:
                    ans += 1
            res.append(ans)
        return res

    def minCharFreq(self, s: str) -> int:
        if not s:
            return 0
        min_char = 'z'
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
            min_char = min(c, min_char)
        return count[min_char]


# @lc code=end
