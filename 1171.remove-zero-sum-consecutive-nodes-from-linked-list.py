#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        if not head:
            return head

        fake = ListNode(0)
        fake.next = head
        prefix = 0
        # key = prefix sum
        # value = last node of getting this sum value
        seen = {0: fake}
        cur = head
        while cur:
            prefix += cur.val
            seen[prefix] = cur
            cur = cur.next
        # set the next node to be the last node for a prefix sum
        cur = fake
        prefix = 0
        while cur:
            prefix += cur.val
            # remove nodes in between
            cur.next = seen[prefix].next
            cur = cur.next

        return fake.next


# s = Solution()
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(-2)
# head.next.next.next = ListNode(9)
# head.next.next.next.next = ListNode(-3)
# head.next.next.next.next.next = ListNode(3)
# a = s.removeZeroSumSublists(head)
# print(a)

# @lc code=end
