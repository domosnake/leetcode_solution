#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
from typing import List
from collections import Counter


# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # at most K subarrays can be easily obtained by sliding window
        atMostK = self.subarraysWithAtMostKDistinct(A, K)
        atMostK_minus_1 = self.subarraysWithAtMostKDistinct(A, K - 1)
        return atMostK - atMostK_minus_1

    def subarraysWithAtMostKDistinct(self, A: List[int], K: int) -> int:
        count = Counter()
        res = 0
        # window head
        head = 0
        head_num = 0
        # window tail
        for tail, tail_num in enumerate(A):
            count[tail_num] += 1
            # when window size > K
            # we need to shrink window
            while len(count) > K:
                head_num = A[head]
                count[head_num] -= 1
                # remove head_num when its count is 0
                if count[head_num] == 0:
                    count.pop(head_num)
                # shrink by increasing head
                head += 1
            # why counting window length works here?
            # for [1,2,2,2,3], basically we are counting
            # window = [1] => [1]
            # window = [1,2] => [1,2], [2]
            # window = [1,2,2] => [1,2,2], [2,2], [2]
            # window = [1,2,2,2] => [1,2,2,2], [2,2,2], [2,2], [2]
            # window = [1,2,2,2,3] => size exceeds K, shrink window
            # window = [2,2,2,3] => [2,2,2,3], [2,2,3], [2,3], [3]
            # window tail can't expand, loop ends
            # total subarrays = 1 + 2 + 3 + 4 + 4 = 14
            # this way actually avoids double counting
            res += tail - head + 1
        return res


# @lc code=end
