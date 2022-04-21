#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummyHead = ListNode(0, head)
        prevHead = dummyHead
        for _ in range(m - 1):
            prevHead = prevHead.next

        cur = prevHead.next
        for _ in range(n - m):
            curHead = prevHead.next
            nextNode = cur.next

            prevHead.next = nextNode
            cur.next = nextNode.next
            nextNode.next = curHead
        return dummyHead.next


# s = Solution()
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# print(s.reverseBetween(head, 2, 4))

# @lc code=end
