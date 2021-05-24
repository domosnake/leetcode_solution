#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
from typing import List
from collections import deque


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            right_view = None
            for _ in range(len(q)):
                node = q.popleft()
                if not right_view:
                    right_view = node.val

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            res.append(right_view)

        return res


# @lc code=end
