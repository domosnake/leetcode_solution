#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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


# @lc code=end
