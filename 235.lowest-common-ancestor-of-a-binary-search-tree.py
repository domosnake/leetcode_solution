#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        node = root
        while node:
            # both p and q in left subtree
            if p.val < node.val and q.val < node.val:
                node = node.left
            # both p and q in right subtree
            elif p.val > node.val and q.val > node.val:
                node = node.right
            # p and q on diff sub tree
            else:
                return node
# @lc code=end
