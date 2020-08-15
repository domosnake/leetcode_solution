#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
from typing import List


# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # stupidity check
        if t < 0 or k < 0:
            return False
        # sliding window + bucket
        # |nums(i) - nums(j)| <= t
        # |nums(i)/t - nums(j)/t| <= 1
        # nums(j)/t in (nums(i)/t - 1, nums(i)/t, nums(i)/t + 1)
        bucket = {}
        for i, n in enumerate(nums):
            # in case t = 0, make t = 1
            key = n // max(1, t)
            # check constaint k
            # in case t = 0, addtional check abs(bucket[key - 1] - n) <= t
            if key - 1 in bucket and abs(bucket[key - 1] - n) <= t:
                return True
            if key + 1 in bucket and abs(bucket[key + 1] - n) <= t:
                return True
            if key in bucket:
                return True
            bucket[key] = n
            # manage size of window, remove key out of k distance
            if i >= k:
                bucket.pop(nums[i - k] // max(1, t))
        return False


# @lc code=end
