#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # going forward
        # at each index, we calculate and update the max reachable index
        # initially, you can only reach to 0
        max_reachable_index = 0
        for i, jump in enumerate(nums):
            # check if cur index is reachable, within max_reachable_index
            if i > max_reachable_index:
                # if beyond range, meaning you can't reach here and go further
                return False
            # check if cur index can contribute to max_reachable_index
            max_reachable_index_from_here = i + jump
            # update max_reachable_index if we have more "gas"
            # here you can also use function max(a, b)
            if max_reachable_index_from_here > max_reachable_index:
                max_reachable_index = max_reachable_index_from_here
            # optimization: early return if we can directly reach to the end
            if max_reachable_index >= len(nums) - 1:
                return True

        # program shouldn't reach this line
        # because you either gas out somewhere in the mid,
        # or you can directly leap to the end somewhere in the mid
        return True


# @lc code=end
