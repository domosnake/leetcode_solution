#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List
from heapq import heappop, heappush


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists_naive(self, lists: List[ListNode]) -> ListNode:
        # naive way
        if not lists:
            return None
        fakeHead = ListNode(None)
        tail = fakeHead
        # qc first, remove all none or empty nodes in lists
        nodes = [list for list in lists if list and list.val is not None]

        while True:
            min_nodes = []
            nones = 0
            # loop thru to find min nodes to merge
            for i, cur in enumerate(nodes):
                if not cur:
                    nones += 1
                    continue
                # empty min
                if not min_nodes:
                    min_nodes.append(i)
                else:
                    # find smaller
                    if cur.val < nodes[min_nodes[0]].val:
                        min_nodes.clear()
                        min_nodes.append(i)
                    # same min
                    elif cur.val == nodes[min_nodes[0]].val:
                        min_nodes.append(i)
            # when all items merged, nodes will become nones
            if nones == len(nodes):
                break
            # min nodes found, let's merge
            for i in min_nodes:
                # merge new list
                tail.next = nodes[i]
                tail = tail.next
                # move to next
                nodes[i] = nodes[i].next
        return fakeHead.next

    def mergeKLists_pq(self, lists: List[ListNode]) -> ListNode:
        # use priority queue
        if not lists:
            return []
        q = []
        fakeHead = ListNode(None)
        tail = fakeHead
        for i, node in enumerate(lists):
            if not node:
                continue
            # priority, tie-breaker, item
            # compare priority, if tie, compare i
            heappush(q, (node.val, i, node))
        # merge
        while q:
            v, i, node = heappop(q)
            tail.next = node
            tail = tail.next
            if node.next:
                heappush(q, (node.next.val, i, node.next))
        return fakeHead.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # merge 2 list, then keep merging until only 1 list left
        if not lists:
            return []
        # qc remove none or empty lists
        nodes = [n for n in lists if n and n.val is not None]
        head = None
        for n in (nodes):
            head = self.merge2Lists(head, n)
        return head

    def merge2Lists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a:
            return b
        if not b:
            return a
        fakeHead = ListNode(None)
        tail = fakeHead
        # merge
        while a and b:
            if a.val > b.val:
                min_node = b
                b = b.next
            else:
                min_node = a
                a = a.next
            tail.next = min_node
            tail = tail.next
        # append rest
        if a:
            tail.next = a
        if b:
            tail.next = b
        return fakeHead.next


# @lc code=end
