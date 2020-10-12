#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        if not amount:
            return 0
        # return min number of coins
        # dp - dp[i] = the optimzal way of changing coins given amount i
        # way of changing = min of way of changing - a coin + 1 (this coin)
        # dp[i] = min(dp[i]), dp[i - coin[i]] + 1)
        dp = [0] + [float('inf')] * amount
        for a in range(1, amount + 1):
            for coin in coins:
                # make sure we have enough amount to change a coin
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1
        if not amount:
            return 0
        # return min number of coins
        # bfs + greedy + pruning
        # why bfs?
        # 1. because I know the answer is closer to the search tree root
        #    bfs is faster than dfs
        # 2. bfs is meant to return min path

        # greedy - always try to pick the largest coin
        coins.sort(reverse=True)

        min_count = float('inf')
        # (count, amount)
        queue = deque()
        queue.append((0, amount))
        visited = [True] + [False] * amount
        # bfs
        while queue:
            count, cur_amount = queue.popleft()
            count += 1
            for coin in coins:
                remain = cur_amount - coin
                # found a combination
                if remain == 0:
                    return min(min_count, count)
                # coin is too big
                elif remain < 0:
                    continue
                # can have more coins to change
                else:
                    if not visited[remain]:
                        visited[remain] = True
                        queue.append((count, remain))
        return -1


# s = Solution()
# a = s.coinChange([1, 5, 7], 11)
# print(a)

# @lc code=end
