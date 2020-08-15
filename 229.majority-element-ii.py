#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
from typing import List


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # boyer-moore majority voting algoritm
        # at most 2 elements can appear more than n/3 times
        e1, e1_count = None, 0
        e2, e2_count = None, 0
        # first pass to find 2 candidates
        for num in nums:
            if e1 == num:
                e1_count += 1
            elif e2 == num:
                e2_count += 1
            elif e1_count == 0:
                e1 = num
                e1_count += 1
            elif e2_count == 0:
                e2 = num
                e2_count += 1
            # this step is confusing, why it works
            # because if there exists only e1 and count(e1) > n/3
            # then e1_count would never be reduced to 0
            # if there are 2 candidates, e1, e2 with count > n/3
            # then both of them would not be reduced to 0
            # this step is to remove those elements which count <= n/3  
            else:
                e1_count -= 1
                e2_count -= 1
        # second pass to verify e1, e2
        # candidate < n/3 will not be to added to final answer( rejected ) 
        res = [e for e in (e1, e2) if nums.count(e) > len(nums) / 3]
        return res


# @lc code=end
