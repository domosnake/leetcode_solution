#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#
from collections import deque


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
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # check if linked list is a parent-to-child path in the tree
        if not head or not root:
            return False
        q = deque()
        q.append(root)
        # bfs for each node
        while q:
            node = q.popleft()
            # dfs to valid the path
            if self.dfs(head, node):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False

    def dfs(self, cur: ListNode, node: TreeNode) -> bool:
        if cur is None:
            return True
        if node is None or cur.val != node.val:
            return False
        return self.dfs(cur.next, node.left) or self.dfs(cur.next, node.right)


# @lc code=end
