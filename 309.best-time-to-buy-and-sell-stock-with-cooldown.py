#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # finite state machine
        # generalize the cooldown to k days
        #
        # we only have 2 states, buy, sell
        # there are solutions use 3 states with an addtional rest state
        # but we can just think that we buy based on the balance before the cooldown
        # e.g. say COOLDOWN = 2
        # today's buy state balance is either yesterday's buy state(no buy)
        # or buy based on the balance 3 days ago(- 1 - COOLDOWN)
        # whichever is higher
        #
        # buy[i] = max(buy[i - 1], sell[i - 1 - cooldown] - prices(i))
        # sell[i] = max(sell[i - 1], buy[i - 1] + price[i])
        # define the cooldown here, for the problem, COOLDOWN = 1
        COOLDOWN = 1
        # to optimize space from O(n) to O(k)
        # we only 2 buy states, buy[0] = prev, buy[1]= cur
        buy = [float('-inf'), 0]
        # we only need sell states with size 2 + COOLDOWN
        # becuase we need to retrieve the balance before cooldown
        # you may ask why I choose pop() and append() to update sell state
        # because I am lazy, pop() and append() can do shifting for me
        sell = [0]
        for i, p in enumerate(prices):
            # pop and retieve the sell state
            if i < COOLDOWN:
                buy[1] = max(buy[0], -p)
            else:
                buy[1] = max(buy[0], sell.pop(0) - p)
            sell.append(max(sell[-1], buy[0] + p))
            # move state for buy
            # note that sell state has been updated by pop(head) and append(tail)
            buy[0] = buy[1]
        # last sell is the max profit we can get after last price
        # time: O(n), space: O(k) where k is number of cooldown
        return sell[-1]

    def maxProfit_more_space(self, prices: List[int]) -> int:
        COOLDOWN = 1
        buy = [float('-inf')] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        for i, p in enumerate(prices):
            if i < COOLDOWN:
                buy[i + 1] = max(buy[i], -p)
            else:
                buy[i + 1] = max(buy[i], sell[i - COOLDOWN] - p)
            sell[i + 1] = max(sell[i], buy[i] + p)
        # time: O(n), space: O(n)
        return sell[-1]


# @lc code=end
