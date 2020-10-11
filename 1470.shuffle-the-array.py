#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#
from typing import List


# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not nums or len(nums) != 2 * n:
            return []
        res = [0] * len(nums)
        j = 0
        for i in range(n):
            res[j] = nums[i]
            res[j + 1] = nums[i + n]
            j += 2
        return res

    def shuffle_one_liner(self, nums: List[int], n: int) -> List[int]:
        if not nums or len(nums) != 2 * n:
            return []
        return [x for y in zip(nums[:n], nums[n:]) for x in y]

    def shuffle_slicing(self, nums: List[int], n: int) -> List[int]:
        if not nums or len(nums) != 2 * n:
            return []
        res = [0] * len(nums)
        res[::2] = nums[:n]
        res[1::2] = nums[n:]
        return res


# @lc code=end
