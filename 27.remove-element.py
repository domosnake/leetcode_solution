#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            if nums[head] != val:
                head += 1
            else:
                # inline swap: python evaluates from right to left for assignment
                # 1. create a tuple for right
                # 2. assign the tuple to left
                nums[head], nums[tail] = nums[tail], nums[head]
                tail -= 1
        return head


# @lc code=end
