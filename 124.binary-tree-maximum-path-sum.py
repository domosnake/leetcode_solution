#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_sum = [float('-inf')]
        self.dfs(root, max_sum)
        return max_sum[0]

    def dfs(self, node, max_sum):
        if not node:
            return 0

        L = max(self.dfs(node.left, max_sum), 0)
        R = max(self.dfs(node.right, max_sum), 0)
        max_sum[0] = max(max_sum[0], L + R + node.val)

        # pick the max sum of subtree
        return node.val + max(L, R)


# s = Solution()
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# a = s.maxPathSum(root)
# print(a)

# @lc code=end
