#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
from heapq import heappop, heappush


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        max_heap = []
        sum_counter = {}
        self._dfs(root, sum_counter)
        for v, freq in sum_counter.items():
            heappush(max_heap, (-freq, v))
        res = []
        max_freq = max_heap[0][0]
        while max_heap:
            freq, v = heappop(max_heap)
            if max_freq == freq:
                res.append(v)
            else:
                return res
        return res

    def _dfs(self, node, sum_counter):
        if not node:
            return 0
        sub_sum = (self._dfs(node.left, sum_counter) +
                   self._dfs(node.right, sum_counter) + node.val)
        sum_counter[sub_sum] = sum_counter.get(sub_sum, 0) + 1
        return sub_sum


# s = Solution()
# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(-5)
# a = s.findFrequentTreeSum(root)
# print(a)

# @lc code=end
