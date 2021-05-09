#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp
        #       c * a * b
        #     0 1 2 3 4 5
        #   0 y n y n y n
        # a 1 n n n y y n
        # a 2 n n n n y n
        # b 3 n n n n n y
        rows = len(s) + 1
        cols = len(p) + 1
        dp = [[False for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = True

        # udpate first row
        for c in range(2, cols):
            dp[0][c] = p[c - 1] == '*' and dp[0][c - 2]

        # update the dp table
        for row in range(1, rows):
            for col in range(1, cols):
                # char index without offset
                r = row - 1
                c = col - 1
                # if cur char matches or is '.'
                if p[c] == s[r] or p[c] == '.':
                    dp[row][col] = dp[row - 1][col - 1]
                # if cur char is '*'
                elif p[c] == '*':
                    if p[c - 1] == s[r] or p[c - 1] == '.':
                        dp[row][col] = dp[row - 1][col] or \
                                        dp[row][col - 1] or \
                                        dp[row][col - 2]
                    # '*' as empty
                    else:
                        dp[row][col] = dp[row][col - 2]

        return dp[-1][-1]


# s = Solution()
# str = 'aab'
# p = 'c*a*b'
# a = s.isMatch(str, p)
# print(a)

# @lc code=end
