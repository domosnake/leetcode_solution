#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = min(buy, prices[i])
        return profit if profit > 0 else 0


# @lc code=end
