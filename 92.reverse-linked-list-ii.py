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
        if not head or not head.next or m == n:
            return head
        # fake head
        fakeHead = ListNode(-1)
        fakeHead.next = head
        pre_reverse = fakeHead
        # find node before to-be-reversed group
        for _ in range(m - 1):
            pre_reverse = pre_reverse.next
        tail = pre_reverse.next

        for _ in range(n - m):
            # save next node
            temp = pre_reverse.next
            # link to tail next
            pre_reverse.next = tail.next
            # set tail to next
            tail.next = tail.next.next
            # set head
            pre_reverse.next.next = temp
        return fakeHead.next

    def build_linked_list(self, list):
        fake_head = ListNode(-1)
        cur = fake_head
        for n in list:
            cur.next = ListNode(n)
            cur = cur.next

        return fake_head.next


s = Solution()
x = [1, 2, 4, 8, 9, 12]
h = s.build_linked_list(x)
a = s.reverseBetween(h, 3, 6)
print(a)

# @lc code=end
