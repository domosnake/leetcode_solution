#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#


# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles <= 0:
            return 0
        drink = numBottles
        empty = numBottles
        while empty >= numExchange:
            exchange = empty // numExchange
            drink += exchange
            # leftover + exchanged new bottles
            empty = empty % numExchange + exchange
        return drink


# s = Solution()
# a = s.numWaterBottles(15, 4)
# print(a)

# @lc code=end
