#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List


# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # monotonic stack
        ans = [0] * len(T)
        stack = []
        for i in reversed(range(len(T))):
            # check if cur temp is warmer than last seen
            while stack and T[stack[-1]] <= T[i]:
                # keep popping lower temp
                stack.pop()
            ans[i] = 0 if not stack else stack[-1] - i
            stack.append(i)

        return ans


# @lc code=end
