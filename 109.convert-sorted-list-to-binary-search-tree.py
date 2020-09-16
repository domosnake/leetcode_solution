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
    def sortedListToBST_array(self, head: ListNode) -> TreeNode:
        # convert to array and build BST
        # as find center in array is O(1)
        if head is None:
            return None
        list = []
        cur = head
        while cur:
            list.append(cur.val)
            cur = cur.next
        root = self.buildBST_array(list, 0, len(list) - 1)
        return root

    def __buildBST_array(self, list: List[int], lo: int, hi: int) -> TreeNode:
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

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        # build BST from inorder
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        # build BST by simulating inorder traversal
        root = self.__buildBST_inorder(head, 0, size - 1)
        return root

    def __buildBST_inorder(self, head: ListNode, lo: int, hi: int) -> TreeNode:
        # base cases
        if lo > hi:
            return None
        if lo == hi:
            return TreeNode(head.val)
        cur = head
        mid = (lo + hi) // 2
        # each recursion , cut the lined list into half
        for _ in range(lo, mid):
            cur = cur.next
        root = TreeNode(cur.val)
        root.left = self.__buildBST_inorder(head, lo, mid - 1)
        root.right = self.__buildBST_inorder(cur.next, mid + 1, hi)
        return root


# @lc code=end
