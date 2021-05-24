#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque()
        q.append(root)
        while q:
            level_count = len(q)
            for i in range(level_count):
                node = q.popleft()
                if i < level_count - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


# @lc code=end
