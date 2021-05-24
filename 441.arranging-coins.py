#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#


# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 0:
            return 0
        remain = n
        for i in range(n + 1):
            if remain < i:
                return i - 1
            elif remain == i:
                return i
            else:
                remain -= i
        return -1


# @lc code=end
