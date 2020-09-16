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
        # build BST from inorder
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # build BST by simulating inorder traversal
        cur = head
        root = self.__buildBST_inorder(cur, 0, length - 1)
        return root

    def __buildBST_inorder(self, curListNode: ListNode, lo: int, hi: int) -> TreeNode:
        if lo > hi:
            return None

        mid = (lo + hi) // 2

        # simulate inorder traversal
        # recursively form the left subtree
        left = self.__buildBST_inorder(curListNode, lo, mid - 1)

        # process the parent node
        node = TreeNode(curListNode.val)
        node.left = left

        curListNode = curListNode.next

        # recursively form the right subtree
        node.right = self.__buildBST_inorder(curListNode, mid + 1, hi)
        return node


s = Solution()
head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(7)
head.next.next.next = ListNode(11)
head.next.next.next.next = ListNode(20)
head.next.next.next.next.next = ListNode(38)
a = s.sortedListToBST(head)
print(a)
# @lc code=end
