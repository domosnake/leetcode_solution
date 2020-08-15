#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit_dp(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # we can have tuned algorithm to solve MAX_TRANSACTION = 2
        # but let's generalize the problem for MAX_TRANSACTION = k
        MAX_TRANSACTION = 2
        # dynamic programing approach
        # profit[d][t] denotes profit until day d with max t transactions
        # we wanna find recursive formula for profit[d][t] with d - 1 and t - 1
        # if we don't trade on day d, it is same as the prev day
        # profit[d][t] = profit[d - 1][t] --- (a)
        # if we trade on day d, then we need to buy on day x before day d
        # profit[d][t] = prices[i] - prices[x] + profit[x][t - 1] --- (b)
        # we are trying to get the max profit[d][t] either from (a) or (b)
        #                    { profit[d - 1][t]
        # profit[d][t] = max |
        #                    { max(prices[d] - prices[x] + profit[x][t - 1]) (0 <= x < d)
        # ===>
        #                    { profit[d - 1][t]
        # profit[d][t] = max |
        #                    { prices[d] + max(profit[x][t - 1] - prices[x]) (0 <= x < d)
        # notice that
        # when t = 1, d = 1
        # we are calculating max(profit[x][t - 1] - prices[x]) for 0 <= x < d
        # profit[0][1 - 1] - prices[0]
        #
        # when t = 1, d = 2
        # we are calculating max(profit[x][t - 1] - prices[x]) for 0 <= x < d
        # profit[0][1 - 1] - prices[0]
        # profit[1][1 - 1] - prices[1]
        #
        # when t = 1, d = 3
        # we are calculating max(profit[x][t - 1] - prices[x]) for 0 <= x < d
        # profit[0][1 - 1] - prices[0]
        # profit[1][1 - 1] - prices[1]
        # profit[2][1 - 1] - prices[2]
        # ...
        # we have repeated calculations here
        # all we need is max(max_balance, profit[d - 1][t - 1] - prices[d - 1])
        # and notice that we only visit 2 rows: profit[someday][t], profit[someday][t - 1]
        # no need to create 2d array
        even_profit = [0] * len(prices)
        odd_profit = [0] * len(prices)

        for t in range(1, MAX_TRANSACTION + 1):
            max_balance = float('-inf')
            for d in range(1, len(prices)):
                # update even profit row using info in odd profit row
                if t % 2 == 0:
                    max_balance = max(max_balance, odd_profit[d - 1] - prices[d - 1])
                    even_profit[d] = max(even_profit[d - 1], prices[d] + max_balance)
                # update odd profit row using info in even profit row
                else:
                    max_balance = max(max_balance, even_profit[d - 1] - prices[d - 1])
                    odd_profit[d] = max(odd_profit[d - 1], prices[d] + max_balance)
        # when all transactions complete, return last cell depending on even or odd
        # time: O(kn) space: O(n)
        if MAX_TRANSACTION % 2 == 0:
            return even_profit[-1]
        else:
            return odd_profit[-1]

    def maxProfit_finite_state_machine(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # we can have tuned algorithm to solve MAX_TRANSACTION = 2
        # but let's generalize the problem for MAX_TRANSACTION = k
        MAX_TRANSACTION = 2
        # finite state machine approach
        # note that each transaction consists of 2 states: buy and sell
        # each state represents the money you have, aka balance
        # first state you have 0 money
        # followed by buy -> sell -> buy -> sell...
        # defaulting buy and sell to int_MIN, why?
        # because we maintain our balance as high as possible to max profit
        # and they will be overwriten by function max() later
        states = [0] + [float('-inf')] * (MAX_TRANSACTION * 2)

        # everyday, you update the states with the price
        for p in prices:
            for j in range(2, len(states), 2):
                # buy state = j - 1
                # balance_after_buy = prev state balance - buy price
                balance_after_buy = states[j - 2] - p
                # buy state, we wanna buy low, spend less
                # if balance_after_buy is higher, we find lower price, should buy
                # else should do nothing
                states[j - 1] = max(states[j - 1], balance_after_buy)

                # sell state = j
                # balance_after_sell = prev state balance + sell price
                balance_after_sell = states[j - 1] + p
                # sell state, we wanna sell high, gain more
                # if balance_after_sell is higher, we find higher price, should sell
                # else should do nothing
                states[j] = max(states[j], balance_after_sell)

        # last state is the balance after k transactions
        # since we start with 0 money, it is our max profit
        # time: O(kn) space: O(k)
        return states[-1]


# @lc code=end
