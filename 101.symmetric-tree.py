#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._dfs(root.left, root.right)

    def _dfs(self, L, R):
        if not L and not R:
            return True
        if (not L and R) or (not R and L):
            return False

        if L.val != R.val:
            return False

        return self._dfs(L.left, R.right) and self._dfs(L.right, R.left)

    def isSymmetric_bfs(self, root: TreeNode) -> bool:
        # bfs, 2 queues to search left and right trees level by level
        if not root:
            return False
        lq = deque()
        rq = deque()
        lq.append(root.left)
        rq.append(root.right)

        while lq and rq:
            if len(lq) != len(rq):
                return False
            # level by level
            for _ in range(len(lq)):
                L = lq.popleft()
                R = rq.popleft()
                if (not L and R) or (not R and L):
                    return False
                if not L and not R:
                    return True

                if L.val != R.val:
                    return False

                if L.left and R.right:
                    lq.append(L.left)
                    rq.append(R.right)
                # false if either is none
                if (not L.left and R.right) or (L.left and not R.right):
                    return False

                if L.right and R.left:
                    lq.append(L.right)
                    rq.append(R.left)
                # false if either is none
                if (not L.right and R.left) or (L.right and not R.left):
                    return False

        return True


# @lc code=end
