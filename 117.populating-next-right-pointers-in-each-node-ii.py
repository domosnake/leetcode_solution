#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
    def connect_queue(self, root: 'Node') -> 'Node':
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

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        next_head = None
        cur = root
        prev = None
        # next level
        while cur:
            # cur level
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        next_head = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        next_head = cur.right
                    prev = cur.right
                # move cur
                cur = cur.next
            # next level
            cur = next_head
            next_head = None
            prev = None
        return root


# s = Solution()
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(7)
# a = s.connect(root)
# print(a)

# @lc code=end
