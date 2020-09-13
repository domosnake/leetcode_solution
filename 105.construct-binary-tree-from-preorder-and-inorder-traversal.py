#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
from typing import List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        # stack, preorder[0] is the root
        root = TreeNode(preorder[0])
        stack = [root]

        i = 0

        for p in range(1, len(preorder)):
            # keep building left subtree
            if stack[-1].val != inorder[i]:
                left = TreeNode(preorder[p])
                stack[-1].left = left
                stack.append(left)
            else:
                temp = None
                # backtrack to parent to build right subtree
                # by popping from stack
                # while loop is exactly backtracking if it's implemented recursively
                while stack and stack[-1].val == inorder[i]:
                    temp = stack.pop()
                    i += 1
                # add right node, and then keep build left subtree
                right = TreeNode(preorder[p])
                temp.right = right
                stack.append(right)

        return root

    def buildTree_range_check(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # time: O(n), space: O(n)
        # use preorder to find parent
        # use inorder to find left/right subtree size
        # keep tracking range of both inorder and preorder
        inRange = (0, len(inorder) - 1)
        preRange = (0, len(preorder) - 1)
        # user hashmap for quick search val's index at inorder
        val_to_index = {}
        for i, v in enumerate(inorder):
            val_to_index[v] = i
        return self.do_buildTree(preRange, inRange, preorder, val_to_index)

    def do_buildTree(self, preRange: (int, int), inRange: (int, int), preorder: List[int], table: {int: int}) -> TreeNode:
        # check range
        if preRange[0] > preRange[1] or inRange[0] > inRange[1]:
            return None

        # parent val, in preorder, parent is the first
        parent_val = preorder[preRange[0]]
        # parent index at inorder
        parent_index = table[parent_val]
        parent = TreeNode(parent_val)

        # left/right subtree size, they are the same in both traversals
        leftSubtreeSize = parent_index - inRange[0]
        rightSubtreeSize = inRange[1] - parent_index
        # left subtree ranges
        leftInRange = (inRange[0], parent_index - 1)
        leftPreRange = (preRange[0] + 1, preRange[0] + leftSubtreeSize)
        # right subtree ranges
        rightInRange = (parent_index + 1, inRange[1])
        rightPreRange = (preRange[1] - rightSubtreeSize + 1, preRange[1])

        parent.left = self.do_buildTree(leftPreRange, leftInRange, preorder, table)
        parent.right = self.do_buildTree(rightPreRange, rightInRange, preorder, table)
        return parent


# @lc code=end
