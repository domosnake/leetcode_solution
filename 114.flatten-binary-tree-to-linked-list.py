#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        self.dfs(root, prev)

    def dfs(self, node, prev):
        if not node:
            return prev
        prev = self.dfs(node.right, prev)
        prev = self.dfs(node.left, prev)
        node.left = None
        node.right = prev
        prev = node
        return prev

    def flatten_pre_order(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        res = []
        self.pre_order(root, res)
        cur = root
        for i in range(1, len(res)):
            cur.left = None
            cur.right = res[i]
            cur = cur.right

    def pre_order(self, node, res):
        if not node:
            return
        res.append(node)
        self.pre_order(node.left, res)
        self.pre_order(node.right, res)


# @lc code=end
