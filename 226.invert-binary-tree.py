#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self._dfs(root)
        return root

    def _dfs(self, node):
        if not node:
            return

        temp = node.left
        node.left = node.right
        node.right = temp

        self._dfs(node.left)
        self._dfs(node.right)


# @lc code=end
