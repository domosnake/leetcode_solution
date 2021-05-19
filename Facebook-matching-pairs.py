# Matching Pairs
# Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s
# and t after swapping exactly two characters within s.
# A swap is switching s[i] and s[j],
# where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively.
# The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
# Note: This means you must swap two characters at different indices.
# Signature
# int matchingPairs(String s, String t)
# Input
# s and t are strings of length N
# N is between 2 and 1,000,000
# Output
# Return an integer denoting the maximum number of matching pairs
# Example 1
# s = "abcd"
# t = "adcb"
# output = 4
# Explanation:
# Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
# Therefore, the number of matching pairs of s and t will be 4.
# Example 2
# s = "mno"
# t = "mno"
# output = 1
# Explanation:
# Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0]
# and s[1] are swapped, making s = "nmo", which shares only "o" with t.


class Solution:
    def matching_pairs(self, s: str, t: str) -> int:
        count = 0
        match_char = set()
        double_match_swap = set()
        unmatch_s = set()
        unmatch_t = set()
        # track the number of char matched after swap
        match_after_swap = 0
        for i in range(len(s)):
            if s[i] == t[i]:
                count += 1
                match_char.add(s[i])
                continue

            # look for a one-char matching swap
            if match_after_swap == 0:
                if (s[i] in unmatch_t or t[i] in unmatch_s
                        or s[i] in match_char or t[i] in match_char):
                    match_after_swap = 1
                unmatch_s.add(s[i])
                unmatch_t.add(t[i])

            # look for a two-char matching swap
            if match_after_swap < 2:
                if t[i] + s[i] in double_match_swap:
                    match_after_swap = 2
                double_match_swap.add(s[i] + t[i])

        # all match
        if count == len(s):
            return count - 2
        if count == len(s) - 1:
            # case 117, 118
            if match_after_swap == 0:
                return count - 1
            # case 111, 118
            else:
                return count

        # check swap match
        if match_after_swap == 1:
            return count + 1
        elif match_after_swap == 2:
            return count + 2
        else:
            return count
