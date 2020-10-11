#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        ones = 0
        zeros = 0
        score = 0
        # count 1s
        for c in s:
            if c == '1':
                ones += 1
        # splitting in from left to right(without the last index)
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(score, zeros + ones)
        return score

    def maxScore_one_pass(self, s: str) -> int:
        # Max( zeroL + oneR )
        # = Max( zeroL - oneL + oneL + oneR )
        # = Max( zeroL - oneL ) + oneTotal
        if not s or len(s) < 2:
            return 0
        ones = 0
        zeros = 0
        left_zero_one_diff = float('-inf')
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1

            if i < len(s) - 1:
                left_zero_one_diff = max(left_zero_one_diff, zeros - ones)
        return left_zero_one_diff + ones

# s = Solution()
# a = s.maxScore('111110')
# print(a)


# @lc code=end
