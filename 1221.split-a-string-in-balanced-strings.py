#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        half_weight = -1
        half = ''
        for c in s:
            if half_weight == -1:
                half = c
                half_weight = 1
            elif c == half:
                half_weight += 1
            else:
                half_weight -= 1
                if half_weight == 0:
                    count += 1
                    half_weight = -1
        return count


# @lc code=end
