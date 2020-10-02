#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # use heap
        # time: O(nlogk)
        min_heap = []
        for n in nums:
            heappush(min_heap, n)
            if len(min_heap) > k:
                heappop(min_heap)
        return abs(min_heap[0])

    def findKthLargest_k_max(self, nums: List[int], k: int) -> int:
        # find max k times
        # time: O(kn)
        mark = {}
        find_max = k < len(nums) // 2
        k = k if find_max else len(nums) - k + 1

        target = 0
        index = 0
        while k > 0:
            target = float('-inf')
            for i, n in enumerate(nums):
                n = n if find_max else -n
                # marked
                if n in mark and i in mark[n]:
                    continue
                if n > target:
                    target = n
                    index = i
            if target not in mark:
                mark[target] = set()
            mark[target].add(index)
            k -= 1
        return abs(target)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # bucket sort
        # time: O(n)
        lo = min(nums)
        hi = max(nums)
        offset = lo
        bucket = [0] * (hi - lo + 1)
        for n in nums:
            bucket[n - offset] += 1
        for i in reversed(range(len(bucket))):
            while bucket[i] > 0:
                bucket[i] -= 1
                k -= 1
                if k == 0:
                    return i + offset

        return float('-inf')

    def findKthLargest_sort(self, nums: List[int], k: int) -> int:
        # naive way is to sort and find kth element
        # time: O(nlogn)
        nums.sort(reverse=True)
        return nums[k - 1]


# s = Solution()
# a = s.findKthLargest([3, 2, 1, 5, 6, 4, 4], 2)
# print(a)

# @lc code=end
