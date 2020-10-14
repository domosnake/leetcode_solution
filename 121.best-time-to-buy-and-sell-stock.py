#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit_2(self, prices: List[int]) -> int:
        # can only one trade, buy and sell
        max_profit = 0
        if len(prices) < 2:
            return max_profit
        # you must first buy a stock, thus buy at first price
        buy_price = float('inf')
        for p in prices:
            buy_price = min(p, buy_price)
            profit = p - buy_price
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit_3(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        # trade once - buy and sell
        profits = [0] * len(prices)
        buy_price = float('inf')
        for i, p in enumerate(prices):
            buy_price = min(buy_price, p)
            profits[i] = p - buy_price
        return max(profits)

    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        buy = float('inf')
        profit = float('-inf')
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p - buy)
        return profit


# @lc code=end
