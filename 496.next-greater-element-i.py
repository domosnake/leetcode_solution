#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
from typing import List


# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # The Next Greater Number of a number x in nums1
        # is the first number on right side of x and also larger than x in nums2
        # num1 is a subset of nums2, thus, all numbers in nums exist in nums2
        if not nums1:
            return []
        res = [-1] * len(nums1)
        # num to index map
        nums2_index = {n: i for i, n in enumerate(nums2)}
        for i, x in enumerate(nums1):
            # search starting from x's index in nums2
            for j in range(nums2_index[x], len(nums2)):
                if nums2[j] > x:
                    res[i] = nums2[j]
                    # found, break
                    break
        return res


# @lc code=end
