#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
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
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # return all root-to-leaf paths
        paths = []
        path = []
        self.dfs(root, sum, paths, path)
        return paths

    def dfs(self, node: TreeNode, remain: int, paths: List[List[int]], path: List[int]):
        if not node:
            return
        path.append(node.val)
        found = False
        if not node.left and not node.right and remain == node.val:
            found = True
            # save copy
            paths.append(path[:])
        # keep dfs subtrees
        if not found:
            self.dfs(node.left, remain - node.val, paths, path)
            self.dfs(node.right, remain - node.val, paths, path)
        # no matter found or not, backtrack
        path.pop()


s = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
a = s.pathSum(root, 22)
print(a)

# @lc code=end
