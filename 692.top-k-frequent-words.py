#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
from typing import List
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def topKFrequent_sort(self, words: List[str], k: int) -> List[str]:
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

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # max heap
        maxHeap = []
        counter = {}
        res = []
        # init counter for keywords
        for w in words:
            if w in counter:
                counter[w] += 1
            else:
                counter[w] = 0
        # push word with count into max heap
        for word, count in counter.items():
            # key1 = -count, larger count goes first
            # key2 = word, lower alphabetical order word goes first
            # item = word
            heappush(maxHeap, (-count, word, word))
        # pop top k max items
        for _ in range(k):
            res.append(heappop(maxHeap)[2])
        return res


# @lc code=end
