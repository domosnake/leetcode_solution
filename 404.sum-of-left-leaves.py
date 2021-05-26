#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves_stack(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        total = 0
        while stack:
            node, is_left = stack.pop()
            if not node.left and not node.right and is_left:
                total += node.val

            if node.left:
                stack.append((node.left, True))

            if node.right:
                stack.append((node.right, False))

        return total

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, False))
        total = 0
        while q:
            for _ in range(len(q)):
                node, is_left = q.popleft()
                if not node.left and not node.right and is_left:
                    total += node.val

                if node.left:
                    q.append((node.left, True))
                if node.right:
                    q.append((node.right, False))

        return total


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# s = Solution()
# a = s.sumOfLeftLeaves(root)
# print(a)

# @lc code=end
