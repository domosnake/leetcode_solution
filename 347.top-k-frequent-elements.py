#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count first
        # then bucket sort
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # index being count of each num
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        # bucket sort
        for num, frequency in count.items():
            bucket[frequency].append(num)

        res = []
        # backwards, pick k items
        i = len(bucket) - 1
        while i > 0:
            while k > 0:
                # not empty
                if bucket[i]:
                    res.append(bucket[i].pop())
                    k -= 1
                else:
                    i -= 1
            break
        return res


s = Solution()
a = s.topKFrequent([1, 1, 1, 2, 3, 2, 3, 4, 5], 3)
print(a)
# @lc code=end
