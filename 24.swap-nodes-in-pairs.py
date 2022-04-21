#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        self._recursive_swap(dummy_head)
        return dummy_head.next

    def _recursive_swap(self, node):
        if node is None or node.next is None or node.next.next is None:
            return

        node1 = node.next
        node2 = node1.next
        node3 = node2.next
        # swap
        node.next = node2
        node2.next = node1
        node1.next = node3
        # move to next
        self._recursive_swap(node.next.next)


# @lc code=end
