# Reverse Operations
# You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements,
# bordered by either end of the list or an odd element.
# For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
# Then, for each subpart, the order of the elements is reversed.
# In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
# The goal of this question is: given a resulting list, determine the original order of the elements.
# Implementation detail:
# You must use the following definition for elements in the linked list:
# class Node {
#     int data;
#     Node next;
# }
# Signature
# Node reverse(Node head)
# Constraints
# 1 <= N <= 1000, where N is the size of the list
# 1 <= Li <= 10^9, where Li is the ith element of the list
# Example
# Input:
# N = 6
# list = [1, 2, 8, 9, 12, 16]
# Output:
# [1, 8, 2, 9, 16, 12]


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def reverse(self, head):
        fake = Node(-1)
        fake.next = head

        cur = head
        prev = fake
        counting = False
        while cur:
            if cur.data % 2 != 0 and not counting:
                prev = prev.next
                cur = cur.next
            elif cur.data % 2 == 0 and not counting:
                counting = True
                cur = cur.next
            elif cur.data % 2 == 0 and counting:
                cur = cur.next
            else:
                counting = False
                self.reverse_subpart(prev, cur)
                prev = cur
                cur = cur.next

        # reverse the subpart ends with tail
        self.reverse_subpart(prev, cur)

        return fake.next

    # reverse nodes between prev and end exclusively
    def reverse_subpart(self, prev, end):
        cur = prev.next
        while cur and cur.next != end:
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

    def build_linked_list(self, list):
        fake_head = Node(-1)
        cur = fake_head
        for n in list:
            cur.next = Node(n)
            cur = cur.next

        return fake_head.next

    def to_list(self, head):
        list = []
        cur = head
        while cur:
            list.append(cur.data)
            cur = cur.next

        return list


s = Solution()
x = [2, 4, 8, 9, 12, 16, 11, 22]
h = s.build_linked_list(x)
a = s.reverse(h)
print(s.to_list(a))
