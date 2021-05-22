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
        cur = root
        stack = []
        res = []
        while cur or stack:
            # keep going left
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # add left, parent
            res.append(cur.val)
            # then go right
            cur = cur.right
        return res


s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
a = s.test(root)
print(a)

# @lc code=end
