#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
from collections import deque


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree_dfs(self, p: TreeNode, q: TreeNode) -> bool:
        return self._dfs(p, q)

    def _dfs(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self._dfs(p.left, q.left) and self._dfs(p.right, q.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        # bfs
        queue = deque()
        queue.append((p, q))
        while queue:
            _p, _q = queue.popleft()
            # check val
            if not (_p and _q) or _p.val != _q.val:
                return False

            # check children
            if _p.left and _q.left:
                queue.append((_p.left, _q.left))
            # False if either one is None
            if (not _p.left and _q.left) or (_p.left and not _q.left):
                return False

            if _p.right and _q.right:
                queue.append((_p.right, _q.right))
            # False if either one is None
            if (not _p.right and _q.right) or (_p.right and not _q.right):
                return False

        return True


# s = Solution()
# p = TreeNode(1)
# p.left = TreeNode(2)
# p.right = TreeNode(3)
# q = TreeNode(1)
# q.left = TreeNode(2)
# q.right = TreeNode(3)
# a = s.isSameTree(p, q)
# print(a)

# @lc code=end
