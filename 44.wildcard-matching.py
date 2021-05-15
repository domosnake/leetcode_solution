#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp
        #       c * a * b
        #     0 1 2 3 4 5
        #   0 y n n n n n
        # c 1 n y y n n n
        # a 2 n n y y y n
        # d 3 n n y n y n
        # c 4 n n y n y n
        # e 5 n n y n y n
        # b 6 n n y n y y

        rows = len(s) + 1
        cols = len(p) + 1
        dp = [[False for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = True

        # udpate first row
        for c in range(1, cols):
            dp[0][c] = p[c - 1] == '*' and dp[0][c - 1]

        for row in range(1, rows):
            for col in range(1, cols):
                r = row - 1
                c = col - 1
                if p[c] == s[r] or p[c] == '?':
                    dp[row][col] = dp[row - 1][col - 1]
                elif p[c] == '*':
                    dp[row][col] = dp[row][col - 1] or dp[row - 1][col]

        return dp[-1][-1]


# s = Solution()
# str = 'cxyzbpp'
# p = 'c*pppp*'
# a = s.isMatch(str, p)
# print(a)

# @lc code=end
