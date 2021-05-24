#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth_dfs(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        return max(self.dfs(node.left) + 1, self.dfs(node.right) + 1)

    def maxDepth_stack(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return level


# @lc code=end
