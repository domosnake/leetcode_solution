#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # first, notice that we could do this in a naive way
        # e.g. 2^6 = 2 * 2 * 2 * 2 * 2 * 2 = 64 and time is O(n)
        # however, there will be many redundent computions
        # we could think this way 2^6 = 2^3 * 2^3
        # 2^3 = (2^1 * 2^1 * 2)
        # thus, time is O(logn)
        #
        # this is logn optimization problem
        if n == 0:
            return 1
        if x == 0:
            return 0

        if n < 0:
            return 1.0 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


# @lc code=end
