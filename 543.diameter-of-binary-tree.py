#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest = [0]
        self.depth(root, longest)
        return longest[0]

    def depth(self, root, longest):
        if not root:
            return 0
        left = self.depth(root.left, longest)
        right = self.depth(root.right, longest)
        longest[0] = max(longest[0], left + right)
        return 1 + max(left, right)


# s = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# a = s.diameterOfBinaryTree(root)
# print(a)
# @lc code=end
