#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        stack = [(root, root.val)]
        while stack:
            node, cur_sum = stack.pop()
            if node.left:
                stack.append((node.left, cur_sum * 10 + node.left.val))
            if node.right:
                stack.append((node.right, cur_sum * 10 + node.right.val))

            if not node.left and not node.right:
                total += cur_sum
        return total


# @lc code=end
