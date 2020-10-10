#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfit_k_trans_state_machine(prices, 2)

    def maxProfit_k_trans_dp(self, prices: List[int], k: int) -> int:
        if k <= 0 or not prices or len(prices) < 2:
            return 0
        if k >= len(prices):
            k = len(prices)
        # dynamic programing approach
        # profit[t][d] denotes profit until day d with max t transactions
        # we wanna find recursive formula for profit[t][d] with d - 1 and t - 1
        # if we don't trade on day d, it is same as the prev day
        # profit[t][d] = profit[t][d - 1] --- (a)
        #
        # if we trade on day d, then we need to buy on some day x before day d
        # profit[t][d] = prices[i] - prices[x] + profit[x][t - 1] --- (b)
        #
        # we are trying to get the max profit either from (a) or (b)
        #
        #                    { profit[t][d - 1]
        # profit[t][d] = max |
        #                    { max(prices[d] - prices[x] + profit[t - 1][x]) (0 <= x < d)
        # ===>
        #                    { profit[t][d - 1]
        # profit[t][d] = max |
        #                    { prices[d] + max(profit[t - 1][x] - prices[x]) (0 <= x < d)
        # notice that
        # when t = 1, d = 1
        # we are calculating max(profit[t - 1][x] - prices[x]) for 0 <= x < d
        # maxDiff = profit[1 - 1][0] - prices[0]
        #
        # when t = 1, d = 2
        # we are calculating max(profit[t - 1][x] - prices[x]) for 0 <= x < d
        # profit[1 - 1][0] - prices[0]
        # profit[1 - 1][1] - prices[1]
        # maxDiff = max(maxDiff, cur)
        #
        # when t = 1, d = 3
        # we are calculating max(profit[t - 1][x] - prices[x]) for 0 <= x < d
        # profit[1 - 1][0] - prices[0]
        # profit[1 - 1][1] - prices[1]
        # profit[1 - 1][2] - prices[2]
        # maxDiff = max(maxDiff, cur)
        # ...
        # we have repeated calculations here
        # all we need is max(maxDiff, profit[d - 1][t - 1] - prices[d - 1])
        # and notice that we only visit 2 rows: profit[t][someday], profit[t - 1][someday]
        # no need to create 2d array
        profit = []
        for _ in range(k + 1):
            profit.append([0] * len(prices))

        for t in range(1, k + 1):
            max_diff = float('-inf')
            for d in range(1, len(prices)):
                max_diff = max(max_diff, profit[t - 1][d - 1] - prices[d - 1])
                profit[t][d] = max(profit[t][d - 1], prices[d] + max_diff)
        # time: O(k * n) space: O(k * n)
        return profit[-1][-1]

    def maxProfit_k_trans_dp_better_space(self, prices: List[int], k: int) -> int:
        if k <= 0 or not prices or len(prices) < 2:
            return 0
        if k >= len(prices):
            k = len(prices)

        even_profit = [0] * len(prices)
        odd_profit = [0] * len(prices)

        for t in range(1, k + 1):
            max_diff = float('-inf')
            for d in range(1, len(prices)):
                # update even profit row using info in odd profit row
                if t % 2 == 0:
                    max_diff = max(max_diff, odd_profit[d - 1] - prices[d - 1])
                    even_profit[d] = max(even_profit[d - 1], prices[d] + max_diff)
                # update odd profit row using info in even profit row
                else:
                    max_diff = max(max_diff, even_profit[d - 1] - prices[d - 1])
                    odd_profit[d] = max(odd_profit[d - 1], prices[d] + max_diff)
        # when all transactions complete, return last cell depending on even or odd
        # time: O(k * n) space: O(n)
        if k % 2 == 0:
            return even_profit[-1]
        else:
            return odd_profit[-1]

    def maxProfit_k_trans_state_machine(self, prices: List[int], k: int) -> int:
        if k <= 0 or not prices or len(prices) < 2:
            return 0
        if k >= len(prices):
            k = len(prices)
        # finite state machine approach
        # note that each transaction consists of 2 states: buy and sell
        # each state represents the money you have, aka balance
        # first state you have 0 money
        # followed by buy -> sell -> buy -> sell...
        # defaulting buy and sell to int_MIN, why?
        # because we maintain our balance as high as possible to max profit
        # and they will be overwriten by function max() later
        #
        # init -> buy -> sell -> buy -> sell...
        balance = [0] + [float('-inf')] * k * 2
        # everyday, you update the states with the price
        for p in prices:
            for i in range(2, len(balance), 2):
                # for each balancing at i, we have 2 states: buy and sell
                #
                # buy state = i - 1
                # balance_after_buy = prev state balance - buy price
                balance_after_buy = balance[i - 2] - p
                # buy state, we wanna buy low, spend less
                # if balance_after_buy is higher, we find lower price, should buy
                # else should do nothing
                balance[i - 1] = max(balance[i - 1], balance_after_buy)

                # sell state = i
                # balance_after_sell = prev state balance + sell price
                balance_after_sell = balance[i - 1] + p
                # sell state, we wanna sell high, gain more
                # if balance_after_sell is higher, we find higher price, should sell
                # else should do nothing
                balance[i] = max(balance[i], balance_after_sell)

        # last state is the balance after k transactions
        # since we start with 0 money, it is our max profit
        # time: O(kn) space: O(k)
        return balance[-1]


# s = Solution()
# a = s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
# print(a)

# @lc code=end
