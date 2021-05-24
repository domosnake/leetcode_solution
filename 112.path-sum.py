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
        if not root:
            return False
        # must be root-to-leaf path
        return self.dfs(root, root.val, sum)

    def dfs(self, node: TreeNode, total: int, sum: int) -> bool:
        if not node.left and not node.right and total == sum:
            return True

        left = False
        if node.left:
            left = self.dfs(node.left, total + node.left.val, sum)
        right = False
        if node.right:
            right = self.dfs(node.right, total + node.right.val, sum)

        return left or right

    def hasPathSum_stack(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, total = stack.pop()
            if not node.right and not node.left and total == sum:
                return True
            if node.left:
                stack.append((node.left, total + node.left.val))

            if node.right:
                stack.append((node.right, total + node.right.val))

        return False


# @lc code=end
