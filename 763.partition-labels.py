#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
from typing import List


# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        parts = []
        last_index = {s: i for i, s in enumerate(S)}
        window_start_at = 0
        window_end_at = 0
        for i, s in enumerate(S):
            # expand the window to last index of cur char
            if last_index[s] > window_end_at:
                window_end_at = last_index[s]
            # this means we reach to window end
            # we will NOT see any char in the window again beyong this point
            if i == window_end_at:
                parts.append(window_end_at - window_start_at + 1)
                # new window should start next index
                window_start_at = i + 1

        return parts


# @lc code=end
