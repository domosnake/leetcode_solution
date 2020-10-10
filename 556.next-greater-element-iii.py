#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#


# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # positive 32-bit integer n
        s = list(str(n))
        n = len(s)

        i = n - 2
        j = n - 1
        # from the right find the first digit that is
        # smaller than the digit next to it.
        while i >= 0 and s[i + 1] <= s[i]:
            i -= 1

        # all digits sorted in descending order
        # e.g. 4321, no possible nextGreaterElement
        if i == -1:
            return -1

        # find next greater digit on right side of ith digit
        while s[j] <= s[i]:
            j -= 1

        # swap i and j
        s[i], s[j] = s[j], s[i]

        # reverse the right side of ith digit to
        # e.g. after 4 <-> 6, 536974 -> 536479
        s = s[:i + 1] + s[i + 1:][::-1]
        res = int(''.join(s))

        # edge case
        if res > 2**31 - 1 or res == n:
            return -1
        return res


# @lc code=end
