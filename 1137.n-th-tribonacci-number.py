#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 0:
            return -1
        # dp
        slide = [0, 1, 1]
        next = 0
        if n in range(len(slide)):
            return slide[n]
        # sliding as n increases
        for _ in range(len(slide), n + 1):
            next = sum(slide)
            slide[0] = slide[1]
            slide[1] = slide[2]
            slide[2] = next
        return next


# @lc code=end
