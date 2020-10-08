#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#


# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = [0] * 37
        maxCount = 0
        res = 0
        for i in range(1, n + 1):
            d_sum = self.digitSum(i)
            group[d_sum] += 1
            if maxCount < group[d_sum]:
                maxCount = group[d_sum]
                res = 1
            elif maxCount == group[d_sum]:
                res += 1
        return res

    def digitSum(self, n: int) -> int:
        res = 0
        while n > 0:
            d = n % 10
            res += d
            n //= 10
        return res


# @lc code=end
