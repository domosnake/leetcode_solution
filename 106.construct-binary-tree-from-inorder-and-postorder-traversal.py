#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        # stack, which means this can be solved recursively
        root = TreeNode(postorder[-1])
        stack = [root]

        i = len(inorder) - 1

        for p in reversed(range(len(postorder) - 1)):
            # keep building right subtree
            if stack[-1].val != inorder[i]:
                right = TreeNode(postorder[p])
                stack[-1].right = right
                stack.append(right)
            else:
                temp = None
                # backtrack to parent to build left subtree
                # by popping from stack
                # while loop is exactly backtracking if it's implemented recursively
                while stack and stack[-1].val == inorder[i]:
                    temp = stack.pop()
                    i -= 1
                # add left node, and then keep build right subtree
                left = TreeNode(postorder[p])
                temp.left = left
                stack.append(left)

        return root

    def buildTree_range_check(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # time: O(n), space: O(n)
        # use postorder to find parent
        # use inorder to find left/right subtree size
        # keep tracking range of both inorder and postorder
        inRange = (0, len(inorder) - 1)
        postRange = (0, len(postorder) - 1)
        # user hashmap for quick search val's index at inorder
        val_to_index = {}
        for i, v in enumerate(inorder):
            val_to_index[v] = i
        return self.do_buildTree(postRange, inRange, postorder, val_to_index)

    def do_buildTree(self, postRange: (int, int), inRange: (int, int), postorder: List[int], table: {int: int}) -> TreeNode:
        # check range
        if postRange[0] > postRange[1] or inRange[0] > inRange[1]:
            return None

        # parent val, in postorder, parent is the last
        parent_val = postorder[postRange[1]]
        # parent index at inorder
        parent_index = table[parent_val]
        parent = TreeNode(parent_val)

        # left/right subtree size, they are the same in both traversals
        leftSubtreeSize = parent_index - inRange[0]
        rightSubtreeSize = inRange[1] - parent_index
        # left subtree ranges
        leftInRange = (inRange[0], parent_index - 1)
        leftPostRange = (postRange[0], postRange[0] + leftSubtreeSize - 1)
        # right subtree ranges
        rightInRange = (parent_index + 1, inRange[1])
        rightPostRange = (postRange[1] - rightSubtreeSize, postRange[1] - 1)

        parent.left = self.do_buildTree(leftPostRange, leftInRange, postorder, table)
        parent.right = self.do_buildTree(rightPostRange, rightInRange, postorder, table)
        return parent


# @lc code=end
