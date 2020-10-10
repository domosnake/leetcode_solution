#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#
from typing import List


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # return 0 if no nextLargerNode
        if head is None:
            return []

        list = []
        while head:
            list.append(head.val)
            head = head.next

        res = [0] * len(list)
        stack = []
        for i in reversed(range(len(list))):
            while stack and stack[-1] <= list[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(list[i])
        return res


s = Solution()
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)
a = s.nextLargerNodes(head)
print(a)

# @lc code=end
