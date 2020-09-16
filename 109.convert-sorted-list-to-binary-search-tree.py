#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
from typing import List


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # convert to array and build BST
        # as find center in array is O(1)
        if head is None:
            return None
        list = []
        cur = head
        while cur:
            list.append(cur.val)
            cur = cur.next
        root = self.buildBST(list, 0, len(list) - 1)
        return root

    def buildBST(self, list: List[int], lo: int, hi: int) -> TreeNode:
        if lo > hi:
            return None
        # Middle element forms the root.
        mid = (lo + hi) // 2
        node = TreeNode(list[mid])
        if lo == hi:
            return node
        # keep building bst for left and right subtree
        node.left = self.buildBST(list, lo, mid - 1)
        node.right = self.buildBST(list, mid + 1, hi)
        return node


# @lc code=end
