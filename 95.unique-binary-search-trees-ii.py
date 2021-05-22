#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
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
    def generateTrees_recursive(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []

        return self._buildBST(1, n)

    def _buildBST(self, start, end):
        trees = []
        if start > end:
            trees.append(None)
            return trees

        for root_val in range(start, end + 1):

            left_subtrees = self._buildBST(start, root_val - 1)
            right_subtrees = self._buildBST(root_val + 1, end)

            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(root_val, left_subtree, right_subtree)
                    trees.append(root)

        return trees

    # use dp to store the previous small BST trees, and use them to build big trees
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []
        # base:
        # 0 node: empty trees
        # 1 node: 1 tree
        dp = [[None], [TreeNode(1)]]

        # build trees from 2...n nodes, bottom up
        for cur_n in range(2, n + 1):
            # store all the trees for current n
            trees = []
            # choose 1...cur_n as root value
            for root_val in range(1, cur_n + 1):
                # left children number
                left_num = root_val - 1
                # right children number
                right_num = cur_n - root_val
                left_offset = 0
                right_offset = root_val
                # take left subtrees from dp and attach them to root's left
                for left_sub in dp[left_num]:
                    copy_left_sub = self._copyTree(left_sub, left_offset)
                    # take right subtrees from dp and attach them to root's right
                    for right_sub in dp[right_num]:
                        copy_right_sub = self._copyTree(right_sub, right_offset)
                        root = TreeNode(root_val, copy_left_sub, copy_right_sub)
                        trees.append(root)
            # build all trees for current n, update dp
            dp.append(trees)

        return dp[n]

    def _copyTree(self, root, offset):
        if not root:
            return None

        q = deque()
        # copy root
        copy = TreeNode(root.val + offset)
        q.append((root, copy))

        # bfs to copy the entire tree
        # can dfs to copy the tree, but bfs is easier to debug
        while q:
            cur, cur_copy = q.popleft()

            if cur.left:
                # copy left child
                cur_copy.left = TreeNode(cur.left.val + offset)
                q.append((cur.left, cur_copy.left))

            if cur.right:
                # copy right child
                cur_copy.right = TreeNode(cur.right.val + offset)
                q.append((cur.right, cur_copy.right))

        return copy


# s = Solution()
# a = s.generateTrees_dp(3)
# print(len(a))

# @lc code=end
