#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # must be root-to-leaf path
        return self.dfs(root, sum)

    def dfs(self, node: TreeNode, remain: int) -> bool:
        if not node:
            return False
        if not node.left and not node.right and remain == node.val:
            return True
        return self.dfs(node.left, remain - node.val) or self.dfs(node.right, remain - node.val)

# @lc code=end
