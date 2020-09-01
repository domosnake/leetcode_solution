#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import List
from collections import deque


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # this is NOT a sliding window problem
        # in fact, this asks us to find max number in the subarray
        # as it's sliding through the list
        #
        # Solution 1: Brute Force
        # time: O(nk) - linear search to find max in every window of size k
        #
        # Solution 2: maxheap
        # time: O(nlogk) - find max with heap to avoid linear search
        #
        # Solution 3: double-ende queue / monotonic queue
        # time: amortized O(n) - in every window of size k, finding max takes O(1)
        window = MonotonicQueue()
        res = []
        # fill window first
        for i in range(k):
            window.push(nums[i])
        # add first max
        res.append(window.peak())
        # sliding window
        for i in range(k, len(nums)):
            window_head = nums[i - k]
            window_tail = nums[i]
            # add new num
            window.push(window_tail)
            # pop window head
            window.popif(window_head)
            res.append(window.peak())
        return res


class MonotonicQueue:
    # similar to queue, except we will maintain its monotonicity
    # thus, it's either monotonically increasing or monotonically decreasing
    # default is monotonically decreasing, flipping signs to change monotonicity
    #
    # in fact, it can be implemented with a double linked list(head and tail)
    def __init__(self):
        self.q = deque()

    # push to the tail of the queue
    def push(self, num: int):
        # make sure queue is monotonic
        while self.q and num > self.q[-1]:
            self.q.pop()
        self.q.append(num)

    # pop head of the queue, always max
    def pop(self) -> int:
        return self.q.popleft()

    # pop head if head is num
    def popif(self, num: int):
        if self.q and self.q[0] == num:
            self.q.popleft()

    # peak head of the queue, always max
    def peak(self) -> int:
        return self.q[0]


# @lc code=end
