#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self._dfs(nums, [], subsets)
        return subsets

    def _dfs(self, nums, subset, subsets):
        subsets.append(subset[::])
        for i in range(len(nums)):
            self._dfs(nums[i+1:], subset + [nums[i]], subsets)

    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        binary = [0 for _ in range(len(nums))]
        subsets = []
        for _ in range(2**len(nums)):
            subsets.append(
                [nums[i] for i, bit in enumerate(binary) if bit == 1])
            self._addOne(binary)
        return subsets

    def _addOne(self, binary):
        for i in reversed(range(len(binary))):
            binary[i] += 1
            # carry
            if binary[i] == 2:
                binary[i] = 0
            else:
                return


# s = Solution()
# a = [1, 2, 3]
# print(s.subsets(a))

# @lc code=end
