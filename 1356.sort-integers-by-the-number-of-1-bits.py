#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
#
from typing import List


# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda n: (self.onesInBinary(n), n))

    def onesInBinary(self, n: int) -> int:
        ones = 0
        while n > 0:
            if n % 2 != 0:
                ones += 1
            n //= 2
        return ones


# s = Solution()
# a = s.sortByBits([0,1,2,3,4,5,6,7,8])
# print(a)

# @lc code=end
