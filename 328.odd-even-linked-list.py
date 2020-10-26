#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        odd_runner = head
        even_runner = head.next

        odd_head = odd_runner
        even_head = even_runner
        odd = odd_head
        even = even_head
        while even_runner and even_runner.next:
            odd_runner = odd_runner.next.next
            even_runner = even_runner.next.next
            odd.next = odd_runner
            even.next = even_runner
            odd = odd.next
            even = even.next
        # connect odd and even
        odd.next = even_head
        return odd_head


# @lc code=end
