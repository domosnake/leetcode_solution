#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # The overall run time complexity is O(log(m+n))
        # note that median is the "middle" value of a sorted data set
        # for example, for list [1, 2, 3, 4, 5], the median is 3
        #
        # log(m+n) means some kind of binary search over the 2 sorted lists
        # in fact, let's do binary search on index to partition 2 lists
        # so that nums on left are smaller than nums on right side
        # size of left = size of right
        # median = (max(left) + min(right)) / 2

        # force size nums1 > size nums2
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        # at this point nums1 is longer than nums2
        # to ensure how we can cut both lists safely
        # we always cut in the shorter list
        longer = len(nums1)
        shorter = len(nums2)

        lo = 0
        hi = shorter
        while lo <= hi:
            # here shorter -> nums2, longer -> nums1
            cut_index_shorter = (lo + hi) // 2
            # plus 1 to compute cut index safely
            cut_index_longer = (shorter + longer + 1) // 2 - cut_index_shorter

            left_max_1 = nums1[cut_index_longer - 1] if cut_index_longer else float('-inf')
            right_min_1 = nums1[cut_index_longer] if cut_index_longer != longer else float('inf')

            left_max_2 = nums2[cut_index_shorter - 1] if cut_index_shorter else float('-inf')
            right_min_2 = nums2[cut_index_shorter] if cut_index_shorter != shorter else float('inf')

            # we found the mid value because left part is less than right past
            if left_max_1 <= right_min_2 and left_max_2 <= right_min_1:
                if (shorter + longer) % 2 == 0:
                    return (max(left_max_1, left_max_2) + min(right_min_1, right_min_2)) / 2
                # left part have 1 more element
                else:
                    return max(left_max_1, left_max_2)

            # binary search on cutting index
            # we are too far on left side on cutting nums2, push to right
            elif left_max_1 > right_min_2:
                lo = cut_index_shorter + 1
            # we are too far on right side on cutting nums2, push to left
            elif left_max_2 > right_min_1:
                hi = cut_index_shorter - 1

        # reaching here means at least one of input list is not sorted
        return float('-inf')

    def findMedianSortedArrays_merge(self, nums1: List[int], nums2: List[int]) -> float:
        # The overall run time complexity is O(m+n)
        # note that median is the "middle" value of a sorted data set
        # for example, for list [1, 2, 3, 4, 5], the median is 3
        merged = self.mergeSortedArrays(nums1, nums2)
        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2] + merged[(n // 2) - 1]) / 2
        else:
            return merged[n // 2]

    def mergeSortedArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return nums1
        if not nums1:
            return nums2

        merged = []
        i = 0
        j = 0
        while True:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    temp = nums2[j]
                    j += 1
                else:
                    temp = nums1[i]
                    i += 1
                merged.append(temp)
            elif i < len(nums1) and j >= len(nums2):
                merged.append(nums1[i])
                i += 1
            elif i >= len(nums1) and j < len(nums2):
                merged.append(nums2[j])
                j += 1
            else:
                # merge complete
                break
        return merged


s = Solution()
a = s.findMedianSortedArrays([1, 2, 5, 6, 8, 10, 11, 12], [3, 4, 7, 9, 13, 14, 15, 16, 17, 18, 19, 20])
print(a)
a = s.findMedianSortedArrays_merge([1, 2, 5, 6, 8, 10, 11, 12], [3, 4, 7, 9, 13, 14, 15, 16, 17, 18, 19, 20])
print(a)

# @lc code=end
