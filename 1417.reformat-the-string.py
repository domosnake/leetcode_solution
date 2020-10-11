#
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
#


# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        if not s:
            return ''
        letters = []
        digits = []
        res = ''
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                letters.append(c)
        # pigeonhole
        if abs(len(letters) - len(digits)) > 1:
            return res
        return self.alternating_merge(letters, digits)

    def alternating_merge(self, dividers, pigeons) -> str:
        if len(pigeons) > len(dividers):
            return self.alternating_merge(pigeons, dividers)
        res = [None] * (len(dividers) + len(pigeons))
        res[::2] = dividers
        res[1::2] = pigeons
        return ''.join(res)


# @lc code=end
