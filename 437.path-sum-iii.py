#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
from collections import defaultdict


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # path doesn't have to start from root to leaf
        # any path is valid as long as:
        # 1. from parent to child
        # 2. path sum up to target sum
        #
        # brute force is traverse the tree via bfs or dfs
        # for each node, run pathSum to count all paths from current node
        # time: O(n^2)
        #
        # there are a lot of repeated computations
        # which can be optimized by memorizing intermediate result
        # only traverse the tree once
        # time: O(n)
        lookup = defaultdict(int)
        lookup[0] = 1
        paths = self.dfs(root, 0, sum, lookup)
        return paths

    def dfs(self, node: TreeNode, curPathSum: int, target: int, lookup: {int: int}) -> int:
        if not node:
            return 0
        curPathSum += node.val
        # see if we can find complement from previous computed result set
        complement = curPathSum - target
        pathsEndAtCurNode = lookup[complement]
        # update lookup
        lookup[curPathSum] += 1
        # check left and right subtree
        left = self.dfs(node.left, curPathSum, target, lookup)
        right = self.dfs(node.right, curPathSum, target, lookup)
        # backtrack
        lookup[curPathSum] -= 1
        return pathsEndAtCurNode + left + right

    # traverse the tree by bfs
    def pathSum_brute_force_bfs(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        queue = [root]
        paths = 0
        while queue:
            cur = queue.pop()
            # count path from cur node
            paths += self.dfs_check_path_sum(cur, sum)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return paths

    # traverse the tree by dfs
    def pathSum_brute_force_dfs(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        # keep dfs
        pathsFromCurNode = self.dfs_check_path_sum(root, sum)
        left = self.pathSum_brute_force_dfs(root.left, sum)
        right = self.pathSum_brute_force_dfs(root.right, sum)
        return pathsFromCurNode + left + right

    # for each tree node, count paths
    def dfs_check_path_sum(self, node: TreeNode, remain: int) -> int:
        if not node:
            return 0
        if node.val == remain:
            return 1
        left = self.dfs_check_path_sum(node.left, remain - node.val)
        right = self.dfs_check_path_sum(node.right, remain - node.val)
        return left + right


s = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
a = s.pathSum(root, 1)
print(a)
a = s.pathSum_brute_force_bfs(root, 1)
print(a)
a = s.pathSum_brute_force_dfs(root, 1)
print(a)

# @lc code=end
