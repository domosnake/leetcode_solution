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
            # left sub tree
            if p.val < node.val and q.val < node.val:
                node = node.left
            # right sub tree
            elif p.val > node.val and q.val > node.val:
                node = node.right
            # node1 and node2 on diff sub tree
            else:
                return node
# @lc code=end
