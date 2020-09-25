#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        invalidNodes = set()
        self.findInvalidNodes(root, TreeNode(float('-inf')), TreeNode(float('inf')), invalidNodes)
        self.swapInvalidNodes(invalidNodes)

    def findInvalidNodes(self, node: TreeNode, lower: TreeNode, upper: TreeNode, invalidNodes: {TreeNode}):
        if not node:
            return
        if lower.val >= node.val:
            invalidNodes.add(lower)
            invalidNodes.add(node)
        if node.val >= upper.val:
            invalidNodes.add(upper)
            invalidNodes.add(node)

        self.findInvalidNodes(node.left, lower, node, invalidNodes)
        self.findInvalidNodes(node.right, node, upper, invalidNodes)

    def swapInvalidNodes(self, nodes: {TreeNode}):
        if not nodes:
            return
        minNode = min(nodes, key=lambda node: node.val)
        maxNode = max(nodes, key=lambda node: node.val)
        minNode.val, maxNode.val = maxNode.val, minNode.val


s = Solution()
root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(3)
s.recoverTree(root)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
s.recoverTree(root)

root = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(1)
s.recoverTree(root)

root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
s.recoverTree(root)

root = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.left.left = TreeNode(2)
s.recoverTree(root)
print('end')

# @lc code=end
