#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # patience sort: buckets/piles + binary search
        # O(nlogn)
        if not nums:
            return 0
        piles = []
        for n in nums:
            i = 0
            j = len(piles)
            # find the pile to add n
            while i != j:
                mid = (i + j) // 2
                if piles[mid][-1] < n:
                    i = mid + 1
                else:
                    j = mid
            # add on top of existing pile
            if i == len(piles):
                piles.append([n])
            # add to a new pile
            else:
                piles[i].append(n)
        # to print the LIS, just print the first item of the piles
        return len(piles)

    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        # dp: each dp[i] is the length of LIS
        # state: dp[i] = max(dp[i], dp[j] + 1) where 0 <= j < i
        if not nums:
            return 0
        dp = [1] * len(nums)
        maxLen = 0
        for i, n in enumerate(nums):
            for j in range(i):
                if n > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxLen = max(maxLen, dp[i])
        return maxLen


s = Solution()
a = s.lengthOfLIS_dp([1, 3, 6, 7, 9, 4, 10, 5, 6])
print(a)

# @lc code=end
