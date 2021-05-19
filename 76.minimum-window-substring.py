#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        counter = Counter(t)
        required = len(t)

        start = 0
        end = 0
        min_win = len(s) + 1
        min_win_start = -1

        while end < len(s):
            if s[end] in counter:
                if counter[s[end]] > 0:
                    required -= 1
                counter[s[end]] -= 1

            while required == 0:

                # update min window
                if min_win > end - start + 1:
                    min_win = end - start + 1
                    min_win_start = start

                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        required += 1

                # slide start
                start += 1
            # slide end
            end += 1

        if min_win <= len(s) and min_win_start >= 0:
            return s[min_win_start:min_win_start + min_win]
        else:
            return ''


# s = Solution()
# a = s.minWindow('ADOBECODEBANC', 'ABC')
# print(a)

# @lc code=end
