#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        # in order: left(right) child, parent, right(left)
        # pre order: parent, left(right) child, right(left)
        # post order: left(right) child, right(left), parent
        # level order: bfs
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, node: TreeNode, res: List[int]) -> List[int]:
        if not node:
            return
        res.append(node.val)
        self.preorder(node.left, res)
        self.preorder(node.right, res)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
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
                # add parent, left
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            # then go right
            node = node.right
        return res


# @lc code=end
