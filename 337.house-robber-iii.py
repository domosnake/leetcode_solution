#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
from typing import Tuple


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        # bottom up
        if root is None:
            return 0
        res = self.dfs(root)
        return max(res[0], res[1])

    def dfs(self, node: TreeNode) -> Tuple[int, int]:
        if node is None:
            return (0, 0)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # res = (max on robbing cur, max on NOT robbing cur)
        # rob_cur = rob cur + not rob child
        rob_cur = left[1] + right[1] + node.val
        # not_rob_cur = not rob cur + max left + max right
        not_rob_cur = max(left) + max(right)
        return (rob_cur, not_rob_cur)


# root = TreeNode(4)
# root.left = TreeNode(1)
# root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(3)
# s = Solution()
# a = s.rob(root)
# print(a)

# @lc code=end
