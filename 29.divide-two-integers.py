#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # without using *, / or %
        # return quotient
        # e.g. 10 / 3 = truncate(3.333...) = 3
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        div = abs(dividend)
        by = abs(divisor)

        # fall into (-1, 1), rounding to 0
        if div < by:
            return 0

        # xor
        neg = (divisor < 0) != (dividend < 0)
        quotient = 0

        while div >= by:
            maxBy = by
            timesToMinus = 1
            # keep getting the max multiple of by
            # that div can subtract from
            # e.g. 16 / 3
            # 16 can minus 12, which is 3 * 2^2, q = 4
            # 4 can minus 3, which is 3 * 2^0, q = 4 + 1
            # 1 can not minus 3, return q = 5
            while self.__times2(maxBy) < div:
                maxBy = self.__times2(maxBy)
                timesToMinus = self.__times2(timesToMinus)
            div -= maxBy
            quotient += timesToMinus

        if neg:
            quotient = -quotient

        return quotient

    def __times2(self, n: int) -> int:
        return n << 1


s = Solution()
a = s.divide(16, 3)
print(a)
# @lc code=end
