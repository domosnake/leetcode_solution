#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#
from typing import List


# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if not words or len(words) < 2:
            return []
        res = []
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res


# @lc code=end
