#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import List


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # cur index
        cur = len(nums1) - 1
        # index m and n in range
        m = m - 1
        n = n - 1
        while m >= 0 or n >= 0:
            # nums1 empty
            if m < 0:
                # copy nums2[0: j] to nums1[0: cur]
                while n >= 0:
                    nums1[cur] = nums2[n]
                    n -= 1
                    cur -= 1
                return
            # nums2 empty
            if n < 0:
                return
            if nums1[m] >= nums2[n]:
                nums1[cur] = nums1[m]
                m -= 1
                cur -= 1
            else:
                nums1[cur] = nums2[n]
                n -= 1
                cur -= 1


# @lc code=end
