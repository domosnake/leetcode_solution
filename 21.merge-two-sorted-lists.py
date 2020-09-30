#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        n1 = l1
        n2 = l2
        fake_head = ListNode(-1)
        cur = fake_head
        while True:
            a = n1 is not None
            b = n2 is not None
            if a and b:
                if n1.val > n2.val:
                    cur.next = n2
                    n2 = n2.next
                else:
                    cur.next = n1
                    n1 = n1.next
                cur = cur.next
            elif a:
                cur.next = n1
                n1 = n1.next
                cur = cur.next
            elif b:
                cur.next = n2
                n2 = n2.next
                cur = cur.next
            else:
                break
        return fake_head.next


s = Solution()
num1 = ListNode(1)
num1.next = ListNode(2)
num1.next.next = ListNode(4)
num2 = ListNode(1)
num2.next = ListNode(3)
num2.next.next = ListNode(4)
a = s.mergeTwoLists(num1, num2)
print(a)


# @lc code=end
