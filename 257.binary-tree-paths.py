#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
from typing import List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths_dfs(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        self.dfs(root, paths, [])
        return paths

    def dfs(self, node, paths, path):
        if not node:
            return

        path.append(str(node.val))
        if not node.left and not node.right:
            paths.append('->'.join(path))

        self.dfs(node.left, paths, path)
        self.dfs(node.right, paths, path)
        # backtrack
        path.pop()

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        stack = [(root, str(root.val) + '->')]

        while stack:
            node, val_str = stack.pop()
            if node.left:
                stack.append((node.left, val_str + str(node.left.val) + '->'))
            if node.right:
                stack.append((node.right, val_str + str(node.right.val) + '->'))

            if not node.left and not node.right:
                paths.append(val_str[:-2])

        return paths


# s = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# a = s.binaryTreePaths(root)
# print(a)

# @lc code=end
