#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        # in order: left(right) child, parent, right(left)
        # pre order: parent, left(right) child, right(left)
        # post order: left(right) child, right(left), parent
        # level order: bfs
        res = []
        self.postorder(root, res)
        return res

    def postorder(self, node: TreeNode, res: List[int]):
        if not node:
            return
        self.postorder(node.left, res)
        self.postorder(node.right, res)
        res.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # in order: left(right) child, parent, right(left)
        # pre order: parent, left(right) child, right(left)
        # post order: left(right) child, right(left), parent
        # level order: bfs
        if not root:
            return []
        res = []
        stack = [root] * 2
        while stack:
            node = stack.pop()
            if stack and stack[-1] is node:
                if node.right:
                    stack += [node.right] * 2
                if node.left:
                    stack += [node.left] * 2
            else:
                res.append(node.val)
        return res


# @lc code=end
