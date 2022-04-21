#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        lent = len(t)
        target = Counter(t)
        min_window = len(s) + 1
        min_win_lo = -1

        lo = 0
        hi = 0
        while hi < len(s):
            # grow
            hi_char = s[hi]
            if hi_char in target:
                if target[hi_char] > 0:
                    lent -= 1
                target[hi_char] -= 1

            while lent == 0:
                # shrink
                if min_window > hi - lo + 1:
                    min_window = hi - lo + 1
                    min_win_lo = lo

                lo_char = s[lo]
                if lo_char in target:
                    target[lo_char] += 1
                    if target[lo_char] > 0:
                        lent += 1

                lo += 1
            hi += 1

        if min_window <= len(s) and min_win_lo >= 0:
            return s[min_win_lo:min_win_lo + min_window]
        else:
            return ''


# s = Solution()
# a = s.minWindow('ADOBECODEBANC', 'ABC')
# print(a)

# @lc code=end
