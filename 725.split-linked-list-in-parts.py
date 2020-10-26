#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
from typing import List


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if k <= 0:
            return []
        if not root:
            return [None] * k
        length = 0
        cur = root
        while cur:
            length += 1
            cur = cur.next

        part_length = length // k
        mod = length % k
        parts = [None] * k
        prev = None
        cur = root
        for i in range(len(parts)):
            parts[i] = cur
            # loop thru a part
            for _ in range(part_length):
                prev = cur
                cur = cur.next
            # if this need to store +1 node
            if mod > 0:
                prev = cur
                cur = cur.next
                mod -= 1
            # break up list
            prev.next = None

        return parts


# @lc code=end
