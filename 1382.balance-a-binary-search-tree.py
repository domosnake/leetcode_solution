#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # turn the BST into a sorted list via inorder traversal
        # and build a balanced BST from the sorted list
        if not root:
            return root
        list = []
        self.__inorder(root, list)
        root = self.__buildBST(list, 0, len(list) - 1)
        return root

    def __inorder(self, root: TreeNode, list: List[int]):
        if not root:
            return
        self.__inorder(root.left, list)
        list.append(root.val)
        self.__inorder(root.right, list)

    def __buildBST(self, list: List[int], lo: int, hi: int) -> TreeNode:
        if lo > hi:
            return None
        if lo == hi:
            return TreeNode(list[lo])
        mid = (lo + hi) // 2
        node = TreeNode(list[mid])
        node.left = self.__buildBST(list, lo, mid - 1)
        node.right = self.__buildBST(list, mid + 1, hi)
        return node

# @lc code=end
