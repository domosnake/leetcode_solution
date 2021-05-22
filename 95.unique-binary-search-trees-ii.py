#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
from typing import List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        return self._buildBST(1, n)

    def _buildBST(self, start, end):
        trees = []
        if start > end:
            trees.append(None)
            return trees

        for root_val in range(start, end + 1):

            left_subtrees = self._buildBST(start, root_val - 1)
            right_subtrees = self._buildBST(root_val + 1, end)

            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(root_val, left_subtree, right_subtree)
                    trees.append(root)

        return trees


# s = Solution()
# a = s.generateTrees(3)
# print(len(a))

# @lc code=end
