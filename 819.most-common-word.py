#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#
from typing import List
from collections import defaultdict
from heapq import heappush, heappop
from re import findall


# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedSet = set(banned)
        counter = defaultdict(int)
        maxHeap = []
        # find only a-z words
        words = findall('[a-z]+', paragraph.lower())
        for w in words:
            if w not in bannedSet:
                counter[w] += 1
                heappush(maxHeap, (-counter[w], w))

        return heappop(maxHeap)[1]


# @lc code=end
