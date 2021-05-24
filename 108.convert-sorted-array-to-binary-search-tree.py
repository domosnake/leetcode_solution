#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        # build a balanced BST tree
        root = self.build(0, len(nums) - 1, nums)
        return root

    def build(self, lo, hi, nums):
        if lo > hi:
            return None
        mid = (hi + lo) // 2
        node = TreeNode(nums[mid])
        node.left = self.build(lo, mid - 1, nums)
        node.right = self.build(mid + 1, hi, nums)
        return node


# s = Solution()
# a = s.sortedArrayToBST([-10,-3,0,5,9])
# print(a)

# @lc code=end
