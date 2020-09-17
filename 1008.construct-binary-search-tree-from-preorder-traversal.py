#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
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
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # note that in perorder, the first item is always the parent
        if not preorder:
            return None
        root = self.buildBST(preorder, 0, len(preorder) - 1)
        return root

    def buildBST(self, preorder: List[int], lo: int, hi: int):
        if lo > hi or lo >= len(preorder) or hi >= len(preorder):
            return None
        if lo == hi:
            return TreeNode(preorder[lo])
        parent = TreeNode(preorder[lo])
        # find right subTree index
        rightLo = lo
        while rightLo < len(preorder) and preorder[lo] >= preorder[rightLo]:
            rightLo += 1
        parent.left = self.buildBST(preorder, lo + 1, rightLo - 1)
        parent.right = self.buildBST(preorder, rightLo, hi)
        return parent


s = Solution()
a = s.bstFromPreorder([8, 10, 12])
print(a)
# @lc code=end
