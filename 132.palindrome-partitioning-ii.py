#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#


# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        # edge cases
        if not s or len(s) <= 1:
            return 0
        if s == s[::-1]:
            return 0
        # build matrix, matrix[i][j] = s[i:j + 1] is a pal?
        n = len(s)
        matrix = [[False for j in range(n)] for i in range(n)]
        # loop diagonally to valid palindrome matrix
        for lvl in range(n):
            for i in range(n - lvl):
                j = i + lvl
                if i == j:
                    matrix[i][j] = True
                elif s[i] == s[j] and abs(j - i) == 1:
                    matrix[i][j] = True
                elif s[i] == s[j] and matrix[i + 1][j - 1]:
                    matrix[i][j] = True
                else:
                    matrix[i][j] = False

        min_cut = self._dp(s, matrix)
        return min_cut

    def _dp(self, s, matrix) -> int:
        n = len(s)
        cut = [float('inf') for _ in range(n)]
        cut[0] = 0
        # [0......j, j+1.......i]
        for i in range(n):
            if matrix[0][i]:
                cut[i] = 0
                continue
            for j in range(i):
                if matrix[j + 1][i]:
                    cut[i] = min(cut[i], cut[j] + 1)
        return cut[n - 1]


# s = Solution()
# a = 'aab'
# res = s.minCut(a)
# print(res)

# @lc code=end
