#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
from typing import List


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if amount < 0 or not coins:
            return 0
        # dp - knapsack problem
        # dp[i] = ways to combinations to make up amount i using previous seen coins
        # dp[i] = sum of (dp[i - coins[j]])
        # e.g. coins = [1, 2, 5]
        #      dp[2] = dp[2 - 1] + dp[2 - 2]
        #            = dp[1] + d[0]
        #            = 1 + 1
        #            = (1, 1) + (2)
        dp = [1] + [0] * amount
        for coin in coins:
            for a in range(1, amount + 1):
                if a - coin >= 0:
                    dp[a] += dp[a - coin]
        return dp[amount]

    def change_dfs(self, amount: int, coins: List[int]) -> int:
        # return number of ways to change coins
        # Input: amount = 5, coins = [1, 2, 5]
        # Output: 4
        # Explanation: there are four ways to make up the amount:
        # 5 = 5
        # 5 = 2 + 2 + 1
        # 5 = 2 + 1 + 1 + 1
        # 5 = 1 + 1 + 1 + 1 + 1
        #
        # dps to find all paths
        if amount == 0:
            return 1
        if amount < 0 or not coins:
            return 0

        memo = {}
        return self.dfs(sorted(coins, reverse=True), 0, amount, memo)

    def dfs(self, coins, start, amount, memo) -> int:
        if amount == 0:
            return 1

        if (start, amount) in memo:
            return memo[(start, amount)]

        ways = 0
        for i in range(start, len(coins)):
            if amount >= coins[i]:
                ways += self.dfs(coins, i, amount - coins[i], memo)

        memo[(start, amount)] = ways
        return ways


# @lc code=end
