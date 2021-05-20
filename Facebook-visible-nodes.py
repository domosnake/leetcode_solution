# Number of Visible Nodes
# There is a binary tree with N nodes.
# You are viewing the tree from its left side and can see only the leftmost nodes at each level.
# Return the number of visible nodes.
#
# Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes.
# The leftmost node at a level could be a right node.
#
# Signature
# int visibleNodes(Node root) {
# Input
# The root node of a tree, where the number of nodes is between 1 and 1000,
# and the value of each node is between 0 and 1,000,000,000
# Output
# An int representing the number of visible nodes.
# Example
#             8  <------ root
#            / \
#          3    10
#         / \     \
#        1   6     14
#           / \    /
#          4   7  13
# output = 4
from collections import deque


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def visible_nodes_bfs(self, root):
        levels = 0
        q = deque()
        q.append(root)

        while q:
            levels += 1

            cur_level_num = len(q)
            for _ in range(cur_level_num):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return levels

    def visible_nodes_dfs(self, root):
        max_level = [-1]
        self._dfs(root, 0, max_level)
        return max_level[0]

    def _dfs(self, node, level, max_level):
        if not node:
            max_level[0] = max(max_level[0], level)
            return

        self._dfs(node.left, level + 1, max_level)
        self._dfs(node.right, level + 1, max_level)
