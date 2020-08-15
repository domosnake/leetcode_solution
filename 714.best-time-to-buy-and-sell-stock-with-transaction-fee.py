#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp
        # assuming we pay fee when selling, which is equivalent to paying when buying
        # buy[i] = max(buy[i-1], sell[i-1] - p)
        # sell[i] = max(sell[i-1], buy[i-1] + p - fee)
        #
        # note that term i relies on term i - 1, let's optimize space to O(1)
        buy = [float('-inf'), 0]
        sell = [0, 0]
        for price in prices:
            buy[1] = max(buy[0], sell[0] - price)
            sell[1] = max(sell[0], buy[0] + price - fee)
            # update states
            buy[0] = buy[1]
            sell[0] = sell[1]
        # time: O(n), space: O(1)
        return sell[-1]

    def maxProfit_greedy(self, prices: List[int], fee: int) -> int:
        # greedy, try to make profit whenever possible
        #
        # we should only trade whenever net profit is greater than 0
        # net profit = sell price - buy price - fee
        # e.g. fee = 3, and we buy at 1, sell at 2
        # our net profit is 2 - 1 - 3 = -2 (don't trade!)
        total_profit = 0
        min_price = float('inf')
        prev_price = prices[0]
        for _, price in enumerate(prices, 1):
            # find min price to buy at
            min_price = min(min_price, prev_price)
            # price goes down, could sell at prev price
            if price < prev_price:
                # but need to check fee, only update positive profit
                net_profit = prev_price - min_price - fee
                if net_profit > 0:
                    total_profit += net_profit
                    # after trade, need to set min price to prev price - fee
                    # why lower the buy price? because if later we find a higher sell price
                    # we wanna merge 2 transcations to 1, thus, we need to avoid double pay fees
                    min_price = prev_price - fee
            # update prev price
            prev_price = price
        # check if last price could increase profit
        total_profit += max(0, prices[-1] - min_price - fee)
        # time: O(n), space: O(1)
        return total_profit


# @lc code=end
