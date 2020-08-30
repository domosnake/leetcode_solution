#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self.dfs(node.left) + 1, self.dfs(node.right) + 1)


# @lc code=end
