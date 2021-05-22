#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#


# @lc code=start
class Solution:
    def numTrees_dp(self, n: int) -> int:
        if n <= 0:
            return 0
        # buttom up
        dp = [1, 1]
        for nodes in range(2, n + 1):
            count = 0
            for left in range(nodes):
                right = nodes - 1 - left
                count += dp[right] * dp[left]

            dp.append(count)

        return dp[n]

    # dp optimized
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        # buttom up
        dp = [1, 1]
        for nodes in range(2, n + 1):
            count = 0
            children = nodes - 1
            left = 0
            right = children - left
            while left < right:
                count += dp[left] * dp[right] * 2
                left += 1
                right -= 1
            # check even/odd
            if left == right:
                count += dp[left] * dp[right]
            dp.append(count)

        return dp[n]


# s = Solution()
# a = s.numTrees(4)
# print(a)

# @lc code=end
