#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # edge cases
        if k <= 0 or not prices or len(prices) < 2:
            return 0
        # when k >> len(price), we may face memory issue
        # in this case, it downgrades to Best Time to Buy and Sell Stock II
        # where you can trade as many times as possile
        if k >= len(prices) - 1:
            total_profit = 0
            for i in range(1, len(prices)):
                # trade or do nothing
                total_profit += max(0, prices[i] - prices[i - 1])
            return total_profit
        # same as Best Time to Buy and Sell Stock III
        # finite state machine
        # each state denotes balance you have
        # initial state(0 money) + buy + sell + buy + sell...
        states = [0] + [float('-inf')] * 2 * k
        for p in prices:
            # each day we update all states
            for i in range(2, len(states), 2):
                # buy state, buy low, spending money
                states[i - 1] = max(states[i - 1], states[i - 2] - p)
                # sell state, sell high, gaining money
                states[i] = max(states[i], states[i - 1] + p)
        return states[-1]


# @lc code=end
