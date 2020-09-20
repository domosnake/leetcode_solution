# Given a binary tree, find the length of the longest consecutive sequence path.
# The path refers to any sequence of nodes from some starting node
# to any node in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# Example 1:
#
# Input:
#
#    1
#     \
#      3
#     / \
#    2   4
#   /   /
#  3   5
#
# Output: 3
#
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:
#
# Input:
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# Output: 2
#
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestSequencePath(self, root: TreeNode) -> int:
        return self.dfs(root, None, 0)

    def dfs(self, node: TreeNode, parent: TreeNode, length: int) -> int:
        if not node:
            return length
        # reset length to = 1
        if parent and node.val != parent.val + 1:
            length = 1
        # otherwise, increment length
        else:
            length += 1
        left = self.dfs(node.left, node, length)
        right = self.dfs(node.right, node, length)
        # return max of cur length or left length or right length
        return max(length, left, right)


s = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.left = TreeNode(2)
root.right.left = TreeNode(3)
a = s.longestSequencePath(root)
print(a)
