#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float('-inf')]
        self.findMaxPathSum(root, res)
        return res[0]

    def findMaxPathSum(self, node: TreeNode, res: List[int]) -> int:
        if node is None:
            return 0

        left_path_sum = max(self.findMaxPathSum(node.left, res), 0)
        right_path_sum = max(self.findMaxPathSum(node.right, res), 0)
        # for node, we can form a path left -> node -> right
        cur_max_path_sum = left_path_sum + node.val + right_path_sum
        res[0] = max(res[0], cur_max_path_sum)

        # when going up, we can only pick one path, either left or right
        return node.val + max(left_path_sum, right_path_sum)


s = Solution()
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
a = s.maxPathSum(root)
print(a)

# @lc code=end
