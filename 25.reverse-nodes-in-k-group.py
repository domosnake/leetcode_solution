#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head
        # fake head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        pre_reverse = head
        groups = 0
        i = 1
        # count groups
        while pre_reverse:
            if i == k:
                i = 0
                groups += 1
            i += 1
            pre_reverse = pre_reverse.next

        # reset pre_reverse and tail for reversing groups
        pre_reverse = fakeHead
        tail = pre_reverse.next
        # loop thru groups
        for _ in range(groups):
            # reverse each group
            for _ in range(k - 1):
                # save next node
                temp = pre_reverse.next
                # link to tail next
                pre_reverse.next = tail.next
                # set tail to next
                tail.next = tail.next.next
                # set head
                pre_reverse.next.next = temp
            # after reversing each group, reset pre_reverse and tail
            pre_reverse = tail
            tail = tail.next
        return fakeHead.next


# @lc code=end
