#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
from typing import Set


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        invalid = set()
        MAX = TreeNode(float('inf'))
        MIN = TreeNode(float('-inf'))
        self._findInvalid(root, MIN, MAX, invalid)
        # swap
        minNode = min(invalid, key=lambda node: node.val)
        maxNode = max(invalid, key=lambda node: node.val)
        minNode.val, maxNode.val = maxNode.val, minNode.val

    def _findInvalid(self, node: TreeNode, lo: TreeNode, hi: TreeNode,
                     invalid: Set[TreeNode]):
        if not node:
            return
        if lo.val >= node.val:
            invalid.add(node)
            invalid.add(lo)
        if node.val >= hi.val:
            invalid.add(hi)
            invalid.add(node)

        self._findInvalid(node.left, lo, node, invalid)
        self._findInvalid(node.right, node, hi, invalid)

    def recoverTree_iterative(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # find the invalid nodes iteratively
        stack = []
        cur = root
        prev = TreeNode(float('-inf'))
        invalid = []

        while cur or stack:
            # go left
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # check prev and cur
            if prev.val >= cur.val:
                invalid.append(prev)
                invalid.append(cur)
            # invalid nodes can only have 3 types:
            # 1 [3 2] 4 -> [3, 2]
            # 1 [4 3 2] 5 -> [4, 3, 3, 2]
            # 1 [5 3 4 2] 6 -> [5, 3, 4, 2]
            # break loop since no need to search any more
            if len(invalid) > 2:
                break
            prev = cur
            cur = cur.right

        # note that for
        # 1 [3 2] 4 -> [3, 2]
        # 1 [4 3 2] 5 -> [4, 3, 3, 2]
        # 1 [5 3 4 2] 6 -> [5, 3, 4, 2]
        # invalid nodes can only be on both ends of the list
        n1 = invalid[0]
        n2 = invalid[-1]
        n1.val, n2.val = n2.val, n1.val


s = Solution()
root = TreeNode(2)
root.left = TreeNode(4)
root.right = TreeNode(3)
s.recoverTree(root)

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.right.left = TreeNode(2)
# s.recoverTree(root)

# root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.right = TreeNode(2)
# s.recoverTree(root)

# root = TreeNode(1)
# root.left = TreeNode(3)
# root.left.right = TreeNode(2)
# s.recoverTree(root)

# root = TreeNode(3)
# root.right = TreeNode(4)
# root.right.left = TreeNode(1)
# root.right.left.left = TreeNode(2)
# s.recoverTree(root)
# print('end')

# @lc code=end
