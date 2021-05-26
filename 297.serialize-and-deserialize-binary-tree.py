#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
from collections import deque


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        data = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                data.append(node.val)
            else:
                data.append(None)
        return '|'.join([str(d) if d is not None else '#' for d in data])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split('|')
        q = deque()
        root = TreeNode(int(data[0]))
        q.append(root)
        for i in range(1, len(data), 2):
            node = q.popleft()
            # left
            if data[i] != '#':
                left = TreeNode(int(data[i]))
                node.left = left
                q.append(left)
            # right
            if i + 1 < len(data) and data[i + 1] != '#':
                right = TreeNode(int(data[i + 1]))
                node.right = right
                q.append(right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.right = TreeNode(-3)
# data = ser.serialize(root)
# data = [
#     4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None,
#     None, 0, 6, 5, None, 9, None, None, -1, -4, None, None, None, -2
# ]
# data = '|'.join([str(d) if d is not None else '#' for d in data])
# ans = deser.deserialize(data)
# back = ser.serialize(ans)
# print(back)
# @lc code=end
