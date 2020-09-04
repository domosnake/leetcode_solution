#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring_map(self, s: str) -> int:
        # sliding window - map
        if not s:
            return 0
        maxLen = 0
        # store char last seen index
        char_last_seen = {}
        start = 0
        for end, c in enumerate(s):
            if c in char_last_seen:
                # update max window length
                maxLen = max(maxLen, end - start)
                # update window start
                start = max(start, char_last_seen[c] + 1)
            # update last seen index
            char_last_seen[c] = end
        # comptue last window length
        maxLen = max(maxLen, end - start + 1)
        return maxLen

    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window - set
        if not s:
            return 0
        maxLen = 0
        # store unique char
        unique_char = set()
        start = 0
        for c in s:
            if c in unique_char:
                # update max window length
                maxLen = max(maxLen, len(unique_char))
                # move start forward by removing head
                while c in unique_char:
                    unique_char.remove(s[start])
                    start += 1
            # add char to set
            unique_char.add(c)
        # comptue last window length
        maxLen = max(maxLen, len(unique_char))
        return maxLen


# @lc code=end
