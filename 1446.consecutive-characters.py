#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#


# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        power = 1
        cur_power = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur_power += 1
            else:
                cur_power = 1
            power = max(power, cur_power)
        return power


# @lc code=end
