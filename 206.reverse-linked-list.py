#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        newHead = None
        cur_node = head
        while cur_node:
            # save next node
            next_node = cur_node.next
            # cur is the new head
            cur_node.next = newHead
            # move new head forward
            newHead = cur_node
            # move cur node next
            cur_node = next_node
        return newHead

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        return self.doReverseRecursive(head, None)

    def doReverseRecursive(self, head: ListNode, newHead: ListNode) -> ListNode:
        if head is None:
            return newHead
        next_node = head.next
        head.next = newHead
        return self.doReverseRecursive(next_node, head)


# @lc code=end
