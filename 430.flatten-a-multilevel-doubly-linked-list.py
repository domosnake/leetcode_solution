#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#


# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        # flattening the linked list means insert the child list if any
        #
        # 1---2---NULL
        # |
        # 3---NULL
        #
        # 1---3---2---NULL
        if not head:
            return head
        cur = head
        # for each node, check if we need to insert child list
        while cur:
            self.insert_child_list(cur, cur.child, cur.next)
            cur = cur.next
        return head

    def insert_child_list(self, parent, child, link_to):
        if child is None:
            return
        cur = child
        # for each node, check if we need to insert child(multi-level) list
        # when done, cur points to the last node of child
        while cur.next:
            self.insert_child_list(cur, cur.child, cur.next)
            cur = cur.next
        # make sure all connections are sorted out
        parent.next = child
        child.prev = parent
        parent.child = None
        cur.next = link_to
        # edge case, if link_to is None, then don't set prev
        if link_to:
            link_to.prev = cur


# s = Solution()
# head = Node(1, None, None, None)
# head.next = Node(2, head, None, None)
# head.child = Node(3, None, None, None)
# a = s.flatten(head)
# print(a)

# @lc code=end
