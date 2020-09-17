# remove all half nodes(one child) a in binary tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeHalfNodes(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if (root.left is not None) != (root.right is not None):
            return None
        self.dfs_remove(root)
        return root

    def dfs_remove(self, node: TreeNode):
        if not node:
            return
        # leaf
        if node.left is None and node.right is None:
            return
        # check left
        if (node.left.left is not None) != (node.left.right is not None):
            node.left = None
        # check right
        if (node.right.left is not None) != (node.right.right is not None):
            node.right = None
        # go left and right
        self.dfs_remove(node.left)
        self.dfs_remove(node.right)


s = Solution()
root = TreeNode(2)
root.left = TreeNode(5)
root.right = TreeNode(7)
root.left.left = TreeNode(6)
root.right.left = TreeNode(11)
root.right.right = TreeNode(18)
a = s.removeHalfNodes(root)
print(a)
