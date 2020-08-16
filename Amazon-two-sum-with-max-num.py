# Given a list of positive integers nums and an int target,
# return indices of the two numbers such that they add up to a target - 30.
#
# Conditions:
#
# You will pick exactly 2 numbers.
# You cannot pick the same element twice.
# If you have muliple pairs, select the pair with the largest number.
# Example 1:
#
# Input: nums = [1, 10, 25, 35, 60], target = 90
# Output: [2, 3]
# Explanation:
# nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
# Example 2:
#
# Input: nums = [20, 50, 40, 25, 30, 10], target = 90
# Output: [1, 5]
# Explanation:
# nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
# nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
# You should return the pair with the largest number.

from typing import List


class Solution:
    def twoSumWithMax(self, nums: List[int], target: int) -> List[int]:
        # two sum, one pass, find max pair
        maxPair = [-1, -1]
        # map index -> value
        hashmap = {}
        OFFSET = 30
        targetSum = target - OFFSET
        for i, n in enumerate(nums):
            complement = targetSum - n
            if complement not in hashmap:
                hashmap[n] = i
            else:
                if abs(n - complement) > abs(maxPair[0] - maxPair[1]):
                    maxPair = [i, hashmap[complement]]

        return maxPair


s = Solution()
nums = [1, 10, 25, 35, 60]
target = 90
a = s.twoSumWithMax(nums, target)
print(a)

nums = [20, 50, 40, 25, 30, 10]
target = 90
a = s.twoSumWithMax(nums, target)
print(a)
