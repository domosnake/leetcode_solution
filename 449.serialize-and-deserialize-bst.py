#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
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
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        data = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            data.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return '|'.join([str(d) for d in data])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        data = data.split('|')
        root = TreeNode(int(data[0]))
        for i in range(1, len(data)):
            val = int(data[i])
            self._insert_to_bst(root, val)

        return root

    def _insert_to_bst(self, root, val):
        if not root:
            return

        node = root
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# root = TreeNode(9)
# root.left = TreeNode(6)
# root.right = TreeNode(11)
# root.left.left = TreeNode(2)
# root.right.right = TreeNode(12)
# root.left.right = TreeNode(7)
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# print(ans)
# @lc code=end
