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
        MAX = float('inf')
        MIN = float('-inf')
        return self.dfs(root, MIN, MAX)

    def dfs(self, cur: TreeNode, lo: int, hi: int) -> bool:
        if not cur:
            return True
        # check this node
        if cur.val <= lo or cur.val >= hi:
            return False
        # dfs, both subtrees must be true
        # lo < left child < node
        # node < right child < hi
        return self.dfs(cur.left, lo, cur.val) and self.dfs(cur.right, cur.val, hi)

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        # inorder traversal of a BST returns non-descending nodes
        # if nodes are not in non-descending order, then its's not a BST
        if not root:
            return True
        stack = []
        cur = root
        prev = TreeNode('-inf')
        while cur or stack:
            # keep going left
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # check if current node > prev node
            if prev.val >= cur.val:
                return False
            prev = cur
            cur = cur.right
        return True


# s = Solution()
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(6)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(7)
# a = s.isValidBST(root)
# print(a)

# @lc code=end
