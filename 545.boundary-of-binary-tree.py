#
#
# [545] Boundary of Binary Tree
# Example:
#
# Input:
#     ____1_____
#    /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10
#
# Ouput:
# [1,2,4,7,8,9,10,6,3]
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundary_binary_tree(self, root: TreeNode) -> List[int]:
        # bfs, but we only care about first and last item per level
        # as well as all leaves
        leftBoundary = []
        rightBounadry = []
        leaves = []
        q = [root]
        while q:
            first = True
            next_level = []
            while q:
                node = q.pop(0)
                # first item, left bound
                if first:
                    leftBoundary.append(node.val)
                    first = False
                # last item, right bound
                elif len(q) == 0:
                    rightBounadry.append(node.val)
                # leaves
                elif node.left is None and node.right is None:
                    leaves.append(node.val)
                # add nodes to next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # add next level to queue
            q += next_level
        # counter-clockwise order, so rightBoundary needs to be reversed
        rightBounadry.reverse()
        return leftBoundary + leaves + rightBounadry


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(10)
a = s.boundary_binary_tree(root)
print(a)
