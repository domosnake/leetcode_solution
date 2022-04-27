#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # find subarray[head, tail] where
        # head is the last index that breaks the order, checking backwards
        # tail is the last index that breaks the order, checking forwards
        head = -1
        max_val = nums[-1]
        # checking backwards
        for i in reversed(range(len(nums) - 1)):
            n = nums[i]
            # order broken, update head
            if n > max_val:
                head = i
            # order intact, update max_val
            else:
                max_val = n

        tail = -1
        min_val = nums[0]
        # checking forwards
        for i in range(1, len(nums)):
            n = nums[i]
            # order broken, update tail
            if n < min_val:
                tail = i
            # order intact, update min_val
            else:
                min_val = n

        # tail, head unchanged, meaning nums is sorted already
        if head == -1 and tail == -1:
            return 0
        return tail - head + 1


# s = Solution()
# a = [2]
# print(s.findUnsortedSubarray(a))
# @lc code=end
