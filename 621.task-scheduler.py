#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
from typing import List


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        max_freq = 0
        max_freq_count = 0
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
            if freq[t] == max_freq:
                max_freq_count += 1
            elif freq[t] > max_freq:
                max_freq = freq[t]
                max_freq_count = 1

        gaps = max_freq - 1
        gap_len = n - (max_freq_count - 1)
        idles = gaps * gap_len
        idles -= len(tasks) - max_freq * max_freq_count
        if idles <= 0:
            return len(tasks)
        else:
            return len(tasks) + idles


# s = Solution()
# a = s.leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "D", "D", "E"], 2)
# # A B C D A B C D E A B
# print(a)


# @lc code=end
