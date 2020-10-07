#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#


# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            step += 1
        return step


# @lc code=end
