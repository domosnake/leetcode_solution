#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher's algorithm
        # check both sides from center
        # but optimized by only picking candidate(vs. all positions) centers
        # time: reduce from O(n^2) to O(n)
        #
        # separate abcd -> #a#b#c#d# to handle even palindromes
        # this way, we can always consider it as finding odd palindormes
        # @ denotes head, $ denotes tail
        separated = '#' + '#'.join(s) + '#'
        # stores the radius of palindrome cernter at each index of separated str
        radius = [0] * len(separated)
        # now this is the key of Manacher's alorithm

        # center index of the current max palindrome
        center = 0
        # right end of the current max palindrome
        rightEnd = 0

        # index in original str
        longest_lo = 0
        longest_hi = 0

        for i in range(len(separated)):
            # when i < right end, this means we can make use of calculated
            # radius[:i] to get radius[i]
            if i < rightEnd:
                # mirror of i with respect to center
                # (i_mirror + i) / 2 = center
                i_mirror = 2 * center - i
                # KEY, there are 3 cases wen updating radius
                # max radius centered at i we can copy from mirror = rightEnd - i
                # case 1: radius[mirror] < rightEnd - i
                #         radius[i] = radius[mirror]
                # case 2: radius[mirror] == rightEnd - i
                #         radius[i] >= rightEnd - i
                #         meaning that radius[i] may and can expand more
                # case 1: radius[mirror] > rightEnd - i
                #         radius[i] >= rightEnd - i
                #         also meaning that radius[i] can expand more
                #
                # considering all 3 cases
                # we will take the min of radius[mirror] and rightEnd - i
                radius[i] = min(radius[i_mirror], rightEnd - i)

            # expand palindrome centered at i to update center and rightEnd
            # the next expand index at lo and hi
            lo = i - radius[i] - 1
            hi = i + radius[i] + 1
            while lo >= 0 and hi < len(separated) and separated[lo] == separated[hi]:
                # update radius
                radius[i] += 1
                lo -= 1
                hi += 1

            # if find new max palindrome so far
            # update center and right_end
            if i + radius[i] > rightEnd:
                center = i
                rightEnd = i + radius[i]
            # update longest palindrome left and right index
            if radius[i] > longest_hi - longest_lo + 1:
                # convert length from separated to original
                # thus, index in '#c#b#c#' to 'cbc'
                longest_lo = (i - radius[i]) // 2
                longest_hi = (i + radius[i] - 1) // 2
        return s[longest_lo: longest_hi + 1]

    def longestPalindrome_expandCenter(self, s: str) -> str:
        # dp - check both sides from center
        # idea is we check each index, and expand palindrome from center
        # update and save longest
        # time: O(n^2)
        longest_lo = 0
        longest_hi = 0
        for i in range(len(s)):
            # odd, center is i
            odd = self.expandPalindrome(s, i, i)
            # even, center is i and i + 1
            even = self.expandPalindrome(s, i, i + 1)
            # cur longest palindrome
            cur_max = odd if odd[1] - odd[0] > even[1] - even[0] else even
            # update longest
            if cur_max[1] - cur_max[0] > longest_hi - longest_lo:
                longest_hi = cur_max[1]
                longest_lo = cur_max[0]
        return s[longest_lo: longest_hi + 1]

    def expandPalindrome(self, s: str, lo: int, hi: int) -> (int, int):
        # expand from center, return the max length of palindrome
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        # lo or hi will be invalid, the real length should be
        # (hi - 1) and (lo + 1)
        return (lo + 1, hi - 1)

    def longestPalindrome_bruteForce(self, s: str) -> str:
        # brute force
        # time: O(n^3) - O(n^2) to get all substrings, O(n) to check each palindrome
        longest_lo = 0
        longest_hi = 0
        # for all possible substrings, check palindrome
        for i in range(len(s)):
            for j in range(i, len(s)):
                # check palindrome only if length is longer than cur longest
                if j - i > longest_hi - longest_lo and self.isPalindrome(s, i, j):
                    longest_lo = i
                    longest_hi = j
        # return substring
        return s[longest_lo: longest_hi + 1]

    def isPalindrome(self, s: str, lo: int, hi: int) -> bool:
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True


# @lc code=end
