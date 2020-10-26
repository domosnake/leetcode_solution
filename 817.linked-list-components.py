#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#
from typing import List


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head or not G:
            return 0
        if len(G) == 1:
            return 1
        groups = 0
        subset = set(G)
        cur = head
        checking = False
        while cur:
            if cur.val in subset:
                if not checking:
                    groups += 1
                    checking = True
            else:
                if checking:
                    checking = False
            cur = cur.next
        return groups


# @lc code=end
