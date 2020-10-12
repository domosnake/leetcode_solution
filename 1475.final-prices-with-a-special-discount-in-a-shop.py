#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#
from typing import List


# @lc code=start
class Solution:
    def finalPrices_brute_force(self, prices: List[int]) -> List[int]:
        # brute force
        final_prices = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            final_prices.append(prices[i] - discount)
        return final_prices

    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        final_prices = prices[:]
        for i in reversed(range(len(prices))):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack:
                final_prices[i] = prices[i] - stack[-1]
            stack.append(prices[i])
        return final_prices


# @lc code=end
