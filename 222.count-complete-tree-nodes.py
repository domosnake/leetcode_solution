#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_level = 0
        nodes_bottom = 0
        while stack:
            node, lvl = stack.pop()
            max_level = max(max_level, lvl)
            if node.right:
                stack.append((node.right, lvl + 1))
            if node.left:
                stack.append((node.left, lvl + 1))

            if not node.left and not node.right:
                # not on bottom
                if lvl < max_level:
                    break
                # on bottom
                else:
                    nodes_bottom += 1

        # 等比数列求和
        return 2**(max_level - 1) + nodes_bottom


# s = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# a = s.countNodes(root)
# print(a)

# @lc code=end
