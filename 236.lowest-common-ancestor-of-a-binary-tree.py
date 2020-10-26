#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left


# s = Solution()
# root = TreeNode(3)
# root.left = TreeNode(5)
# root.right = TreeNode(1)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)
# a = s.lowestCommonAncestor(root, TreeNode(5), TreeNode(4))
# print(a)

# @lc code=end
