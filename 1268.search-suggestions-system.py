#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
from typing import List


# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products or not searchWord:
            return []

        TOP_K = 3
        products_pool = None
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            # means we just typed the 1st char
            if products_pool is None:
                products_pool = sorted([p for p in products if p.startswith(prefix)])
            else:
                products_pool = [p for p in products_pool if p.startswith(prefix)]
            res.append(products_pool[:TOP_K])
        return res


# @lc code=end
