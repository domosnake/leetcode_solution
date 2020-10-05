#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return -1
        cur = head
        res = 0
        while cur:
            res = res * 2 + cur.val
            cur = cur.next
        return res


# @lc code=end
