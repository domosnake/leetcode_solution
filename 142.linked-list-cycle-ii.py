#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        Floyd Cycle Detection Algorithm

        首先假设第一次相遇的时候慢指针走过的节点个数为i，
        设链表头部到环的起点的长度为m，环的长度为n，
        相遇的位置与起点与起点位置距离为k。

        于是有：
        i = m + a * n + k
        其中a为慢指针走的圈数。

        因为快指针的速度是慢指针的2倍，于是又可以得到另一个式子：
        2 * i = m + b * n + k
        其中b为快指针走的圈数。

        两式相减得：
        i = ( b - a ) * n
        也就是说i是圈长的整数倍。

        这是将其中一个节点放在起点，然后同时向前走m步时，
        此时从头部走的指针在m位置。
        而从相遇位置开始走的指针应该在距离起点i+m，i为圈长整数倍，
        则该指针也应该在距离起点为m的位置，即环的起点。
        '''
        if not head or head.next is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # has cycle
            if slow == fast:
                break
        else:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


# @lc code=end
