#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t2:
            return t1
        if not t1:
            return t2
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node

    def mergeTrees_bfs(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t2:
            return t1
        if not t1:
            return t2
        # cover t2 to t1, return t1 in the end
        q1 = [t1]
        q2 = [t2]
        # level by level
        while q1:
            # merge nodes
            node1 = q1.pop(0)
            node2 = q2.pop(0)
            node1.val += node2.val
            # add left children
            if node1.left and not node2.left:
                node2.left = TreeNode()
            elif not node1.left and node2.left:
                node1.left = TreeNode()

            if node1.left and node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
            # add right children
            if node1.right and not node2.right:
                node2.right = TreeNode()
            elif not node1.right and node2.right:
                node1.right = TreeNode()

            if node1.right and node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
        return t1


# @lc code=end
