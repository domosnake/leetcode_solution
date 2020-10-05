#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#


# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n <= 0:
            return -1
        p = 1
        s = 0
        while n > 0:
            d = n % 10
            p *= d
            s += d
            n = n // 10
        return p - s


# @lc code=end
