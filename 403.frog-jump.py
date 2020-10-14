#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False
        # Initially, the frog is on the first stone
        # and assume the first jump must be 1 unit
        #
        # dp[i][k] = ways of jumps to ith stone using k jumps
        # dp[i][k] => dp[i + k - 1][k - 1]
        #          => dp[i + k][k]
        #          => dp[i + k + 1][k + 1]
        offsets = [-1, 0, 1]
        dp = defaultdict(set)
        # start from 0, and first jump is 1
        # reach to 1, with jump 1
        dp[0].add(1)
        dp[1].add(1)
        for i in range(1, len(stones)):
            stone = stones[i]
            # can not reach to cur stone
            if stone not in dp:
                return False
            # all the jumps to cur stone
            for k in dp[stone]:
                # only allow positive jumps
                for jump in [k + o for o in offsets if k + o > 0]:
                    next_pos = stone + jump
                    # found a way to last stone, early return
                    if next_pos == stones[-1]:
                        return True
                    dp[next_pos].add(jump)
        return True


# s = Solution()
# a = s.canCross([0, 2])
# print(a)
# @lc code=end
