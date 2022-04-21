#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
from collections import deque


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        # swap using bfs
        queue = deque()
        queue.appendleft(root)
        while queue:
            node = queue.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return root


# @lc code=end
