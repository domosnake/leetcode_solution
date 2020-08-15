#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
from typing import List


# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        # init counter for keywords
        for w in words:
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 0

        # sort counter by key
        sorted_counter = {k: v for k, v in sorted(counter.items(), key=lambda item: item[0])}
        # sort counter by values(number of occurances)
        res = [k for k, v in sorted(sorted_counter.items(), key=lambda item: item[1], reverse=True)]

        return res[:k]


# @lc code=end
