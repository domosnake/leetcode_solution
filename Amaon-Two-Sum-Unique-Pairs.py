# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target.
# Return the number of pairs.
#
# Example 1:
#
# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:
#
# Input: nums = [1, 1], target = 2
# Output: 1
# Explanation:
# 1 + 1 = 2
# Example 3:
#
# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.
from typing import List


class Solution:
    def twoSumUniquePairs(self, nums: List[int], target: int) -> int:
        # hashmap to save complement
        if not nums:
            return 0
        pairs = 0
        # num counter
        counter = {}
        for n in nums:
            complement = target - n
            if complement in counter:
                if counter[complement] != -1:
                    pairs += 1
                    # invalid both n and complement
                    counter[n] = -1
                    counter[complement] = -1
            else:
                counter[n] = counter.get(n, 0) + 1
        return pairs


s = Solution()
nums = [1, 1, 2, 45, 46, 46]
target = 47
a = s.twoSumUniquePairs(nums, target)
print(a)

nums = [1, 1]
target = 2
a = s.twoSumUniquePairs(nums, target)
print(a)

nums = [1, 5, 1, 5]
target = 6
a = s.twoSumUniquePairs(nums, target)
print(a)
