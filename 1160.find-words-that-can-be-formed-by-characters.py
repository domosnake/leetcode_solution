#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
from typing import List


# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not chars or not words:
            return 0
        length = 0
        count = {}
        for c in chars:
            count[c] = count.get(c, 0) + 1
        for w in words:
            if self.canForm(w, count):
                length += len(w)
        return length

    def canForm(self, word: str, count: {str: int}) -> bool:
        word_count = {}
        for c in word:
            word_count[c] = word_count.get(c, 0) + 1
        for c in word_count.keys():
            if c not in count:
                return False
            if word_count[c] > count[c]:
                return False
        return True


# @lc code=end
