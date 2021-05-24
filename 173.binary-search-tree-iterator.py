#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.inorder = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            self.inorder.append(node.val)
            node = node.right

        self.index = -1

    def next(self) -> int:
        if self.hasNext():
            self.index += 1
            return self.inorder[self.index]
        return float('-inf')

    def hasNext(self) -> bool:
        return 0 <= self.index + 1 < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
