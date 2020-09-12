#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        # we are tryign to avoid the map to reduce space to O(1)
        # fitst pass for next pointer
        # only one list, node followed by copy
        # 1->2->3
        # 1->1'->2->2'->3->3'
        cur = head
        while cur:
            link_to = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = link_to
            cur = link_to
        # second pass for random pointer
        cur = head
        while cur:
            copy_cur = cur.next
            if cur.random:
                copy_cur.random = cur.random.next
            cur = cur.next.next
        # third pass to decouple original and copied list
        cur = head
        copy = cur.next
        while cur:
            copy_cur = cur.next
            cur.next = cur.next.next
            if copy_cur.next:
                copy_cur.next = copy_cur.next.next
            else:
                break
            cur = cur.next
        return copy

    def copyRandomList_naive(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        # nodes to copied nodes map
        node_to_copy = {}
        # fitst pass for next pointer
        copy = Node(head.val)
        copy_cur = copy
        cur = head
        cur = cur.next
        node_to_copy[head] = copy
        while cur:
            copy_cur.next = Node(cur.val)
            copy_cur = copy_cur.next
            node_to_copy[cur] = copy_cur
            cur = cur.next
        # second pass for random pointer
        cur = head
        copy_cur = copy
        while cur:
            to_rand = None
            if cur.random:
                to_rand = node_to_copy[cur.random]
            copy_cur.random = to_rand
            cur = cur.next
            copy_cur = copy_cur.next
        return copy


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.random = head.next.next
head.next.random = head.next.next.next
s = Solution()
a = s.copyRandomList(head)
print(a)


# @lc code=end
