#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
from random import randint


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        Reservoir Sampling where we randomly select k = 1 item from the list
        """
        SAMPLE_SIZE = 1
        count = 0
        reservoir = [0] * SAMPLE_SIZE
        cur = self.head
        for i in range(len(reservoir)):
            reservoir[i] = cur.val
            cur = cur.next
            count += 1
        while cur:
            # 随机获得一个[0, i]内的随机整数
            d = randint(0, count)
            # 如果随机整数落在[0, m-1]范围内，则替换蓄水池中的元素
            if d < SAMPLE_SIZE:
                reservoir[d] = cur.val
            cur = cur.next
            count += 1
        return reservoir[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
