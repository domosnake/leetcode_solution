#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
from typing import List


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # idea is to sort the nums first
        # then loop thru sorted nums
        # there 3 pointers, pointing to cur, next, last
        # if sum is too big, it means we need to find a smaller num, last--
        # if num is too small, it means we need to find a bigger num, next++
        # do above 2 steps for each cur in sorted nums
        nums.sort()
        # cloeset sum to target
        globalSum = None
        for i in range(len(nums)):
            next_i = i + 1
            last_i = len(nums) - 1
            # move inwards
            while next_i < last_i:
                # cur, next, last
                localSum = nums[i] + nums[next_i] + nums[last_i]

                # sum is too small, increament next_i
                if localSum < target:
                    next_i += 1
                # sum is too big, decreament last_i
                elif localSum > target:
                    last_i -= 1
                # find target, diff = 0
                else:
                    return target

                # update global if local is closer
                if globalSum is None:
                    globalSum = localSum
                if abs(localSum - target) < abs(globalSum - target):
                    globalSum = localSum
        return globalSum


# @lc code=end
