#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        # 1st pass, trade space for time
        list = []
        dummyHead = ListNode(0, head)
        cur = dummyHead
        while cur:
            list.append(cur)
            cur = cur.next
        # get the index of prev node
        # note that list = dummyHead + linked list
        m = len(list) - 1 - n
        prevNode = list[m]
        prevNode.next = prevNode.next.next
        return dummyHead.next


# @lc code=end
