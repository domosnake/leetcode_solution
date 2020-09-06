#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # level order = bfs = queue
        if not root:
            return []
        res = []
        q = [root]
        while q:
            next_level = []
            cur_vals = []
            # pop cur level nodes
            while q:
                # pop queue head
                node = q.pop(0)
                cur_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # cur level done
            res.append(cur_vals)
            # append next level nodes to queue
            q += next_level
        return res


# @lc code=end
