# Minimum Length Substrings
# You are given two strings s and t.
# You can select any substring of string s and rearrange the characters of the selected substring.
# Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
#
# Signature
# int minLengthSubstring(String s, String t)
# Input
# s and t are non-empty strings that contain less than 1,000,000 characters each
# Output
# Return the minimum length of the substring of s. If it is not possible, return -1
# Example
# s = "dcbefebce"
# t = "fd"'
# output = 5
# Explanation:
# Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb".
# Thus, the minimum length required is 5.
from collections import Counter


class Solution:
    # similar to leetcode 76
    def min_length_substring(self, s, t):
        # Sliding window
        # Two pointers: moving end forward to find a valid window, moving start forward to find a smaller window
        # Counter and hash map to determine if the window is valid or not
        hashmap = Counter(t)
        start = 0
        end = 0
        # number of char in t in a valid window
        required = len(t)

        min_win_len = float('inf')

        while end < len(s):
            if s[end] in hashmap:
                if hashmap[s[end]] > 0:
                    required -= 1
                hashmap[s[end]] -= 1

            # shrink window
            while required == 0:
                if end - start + 1 < min_win_len:
                    min_win_len = end - start + 1

                if s[start] in hashmap:
                    hashmap[s[start]] += 1
                    if hashmap[s[start]] > 0:
                        required += 1

                start += 1

            end += 1

        if min_win_len == float('inf'):
            return -1
        else:
            return min_win_len


s = Solution()
a = s.min_length_substring('dcbzefebcexf', 'cefe')
print(a)
