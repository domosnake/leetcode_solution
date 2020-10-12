#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#


# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low > high:
            return 0
        nums = (high - low + 1)
        if nums % 2 == 0:
            return nums // 2
        if low % 2 == 0:
            return nums // 2
        else:
            return nums // 2 + 1


# @lc code=end
