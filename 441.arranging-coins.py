#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
from math import sqrt


# @lc code=start
class Solution:
    def arrangeCoins_loop(self, n: int) -> int:
        if n <= 0:
            return 0
        n = n
        for i in range(n + 1):
            if n < i:
                return i - 1
            elif n == i:
                return i
            else:
                n -= i
        return -1

    def arrangeCoins_binary_search(self, n: int) -> int:
        if n <= 0:
            return 0
        hi = 1
        # find upper and lower bound for binary search
        while True:
            total = (1 + hi) * hi // 2
            if n > total:
                hi *= 2
            elif n == total:
                return hi
            else:
                break
        lo = hi // 2
        # binary search
        while lo <= hi:
            mid = (lo + hi) // 2
            total = (1 + mid) * mid // 2
            if n == total:
                return mid
            elif n > total:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi

    def arrangeCoins(self, n: int) -> int:
        # n = (1 + x) * x / 2 -> x^2 + x - 2n = 0
        # solve for x
        if n <= 0:
            return 0
        return int((sqrt(8 * n + 1) - 1) // 2)


# s = Solution()
# a = s.arrangeCoins(12)
# print(a)
# a = s.arrangeCoins(5)
# print(a)
# a = s.arrangeCoins(8)
# print(a)
# a = s.arrangeCoins(1)
# print(a)
# a = s.arrangeCoins(10)
# print(a)
# @lc code=end
