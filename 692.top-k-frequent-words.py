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

    def topKFrequent_heap(self, words: List[str], k: int) -> List[str]:
        # max heap
        maxHeap = []
        counter = {}
        res = []
        # init counter for keywords
        for w in words:
            counter[w] = counter.get(w, 0) + 1
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

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # bucket sort
        # each bucket cell is a min heap
        counter = {}
        res = []
        # init counter for keywords
        for w in words:
            counter[w] = counter.get(w, 0) + 1

        bucket = []
        for _ in range(len(words) + 1):
            bucket.append([])
        # bucket sort
        for word, count in counter.items():
            # key, item, min heap by default
            # word with the lower alphabetical order comes first
            heappush(bucket[count], (word, word))
        # pop top k max items
        i = len(bucket) - 1
        while i > 0:
            while k > 0:
                # not empty
                if bucket[i]:
                    word_with_lower_alpha_order = heappop(bucket[i])[1]
                    res.append(word_with_lower_alpha_order)
                    k -= 1
                else:
                    i -= 1
            break
        return res


s = Solution()
a = s.topKFrequent(["a", "xy", "xy", "a", "b", "b", "c", "x", "x"], 2)
print(a)
# @lc code=end
