#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
from typing import List


# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        # running sum mod: index
        lookup = {0: -1}
        running_sum = 0
        for i in range(len(nums)):
            running_sum = (running_sum + nums[i]) % k
            if running_sum in lookup and i - lookup[running_sum] > 1:
                return True
            if running_sum not in lookup:
                lookup[running_sum] = i
        return False


# s = Solution()
# a = s.checkSubarraySum([23, 2, 4, 6, 7], 6)
# print(a)

# @lc code=end
