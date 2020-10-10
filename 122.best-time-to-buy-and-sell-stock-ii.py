#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit_2(self, prices: List[int]) -> int:
        total_profit = 0
        # max int
        buy_price = float('inf')
        for p in prices:
            buy_price = min(buy_price, p)
            profit = p - buy_price
            # make a transaction, reset buy_price, meaning need to buy again
            if profit > 0:
                total_profit += profit
                buy_price = p
        return total_profit

    def maxProfit(self, prices: List[int]) -> int:
        # trade as many times as you can
        # trade whenever the price goes up
        if not prices or len(prices) < 2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            profit += diff if diff > 0 else 0
        return profit

# @lc code=end
