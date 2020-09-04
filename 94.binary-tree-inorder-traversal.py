#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # in order: left(right) child, parent, right(left)
        # pre order: parent, left(right) child, right(left)
        # post order: left(right) child, right(left), parent
        # level order: bfs
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, node: TreeNode, res: List[int]):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)

    def inorderTraversal_iterative(self, root: TreeNode) -> List[int]:
        # in order: left(right) child, parent, right(left)
        # pre order: parent, left(right) child, right(left)
        # post order: left(right) child, right(left), parent
        # level order: bfs
        node = root
        stack = []
        res = []
        while node or stack:
            # keep going left
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            # add left, parent
            res.append(node.val)
            # then go right
            node = node.right
        return res


# @lc code=end
