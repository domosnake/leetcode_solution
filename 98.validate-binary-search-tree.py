#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, float('-inf'), root.val) and self.dfs(root.right, root.val, float('inf'))

    def dfs(self, node: TreeNode, lower: int, upper: int) -> bool:
        if not node:
            return True
        # check this node
        if not (lower < node.val < upper):
            return False
        # dfs, both subtrees must be true
        return self.dfs(node.left, lower, node.val) and self.dfs(node.right, node.val, upper)

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        # inorder traversal of a BST returns non-descending nodes
        # if nodes are not in non-descending order, then its's not a BST
        if not root:
            return True
        stack = []
        node = root
        prev = None
        while node or stack:
            # keep going left
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev:
                # check if current node > prev node
                if prev.val >= node.val:
                    return False
            prev = node
            node = node.right
        return True


# @lc code=end
