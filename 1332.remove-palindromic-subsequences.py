#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#


# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if self.isPalindrome(s):
            return 1
        return 2

    def isPalindrome(self, s: str) -> bool:
        lo = 0
        hi = len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True


# @lc code=end
