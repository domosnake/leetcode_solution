#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = ListNode(-1)
        cur = fake
        carry = 0
        while l1 or l2:
            d1 = d2 = 0
            if l1:
                d1 = l1.val
                l1 = l1.next
            if l2:
                d2 = l2.val
                l2 = l2.next
            digit_sum = d1 + d2 + carry
            carry = digit_sum // 10
            remain = digit_sum % 10
            # build
            cur.next = ListNode(remain)
            cur = cur.next

        if carry:
            cur.next = ListNode(carry)
        return fake.next

    def print_list(self, n):
        s = ''
        while n:
            if n.next:
                s += str(n.val) + ' -> '
            else:
                s += str(n.val)
            n = n.next
        print(s)


s = Solution()
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(2)
l2 = ListNode(3)
l2.next = ListNode(5)
a = s.addTwoNumbers(l1, l2)
s.print_list(l1)
s.print_list(l2)
s.print_list(a)

# @lc code=end
