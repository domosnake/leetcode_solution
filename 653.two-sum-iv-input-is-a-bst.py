#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        q = deque()
        q.append(root)
        lookup = set()

        while q:
            cur = q.popleft()
            if k - cur.val in lookup:
                return True

            lookup.add(cur.val)

            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)

        return False


# @lc code=end
