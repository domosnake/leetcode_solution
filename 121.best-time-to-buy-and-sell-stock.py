#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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


# @lc code=end
