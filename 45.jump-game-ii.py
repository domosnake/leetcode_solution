#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # going forward one pass
        if len(nums) == 1:
            return 0
        # cur index pointer
        i = 0
        # min jumps needed to reach to the end
        min_jumps = -1
        # initially, max_reachable_index is from index 0
        max_reachable_index = 0
        while i < len(nums):
            # check between cur index and max_reachable_index
            i_next_pos = max_reachable_index + 1
            for j in range(i, i_next_pos):
                max_reachable_index = max(j + nums[j], max_reachable_index)
            min_jumps += 1
            # early return
            if max_reachable_index >= len(nums) - 1:
                return min_jumps + 1
            # update i for next start
            i = i_next_pos

        # shouldn't reach this line, will end at "early return"
        return min_jumps


# @lc code=end
