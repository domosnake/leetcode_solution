#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        balance = [True]
        self.countSubtreeLevel(root, balance)
        return balance[0]

    def countSubtreeLevel(self, node, balance):
        if not node:
            return 0

        left = self.countSubtreeLevel(node.left, balance)
        right = self.countSubtreeLevel(node.right, balance)
        if abs(left - right) > 1:
            balance[0] = False
            return -1

        return max(left, right) + 1


# @lc code=end
