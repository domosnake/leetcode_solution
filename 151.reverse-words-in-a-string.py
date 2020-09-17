#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # no leading or trailing spaces
        # reduce multiple spaces to a single space
        SEP = ' '
        s = s + SEP
        reading_word = False
        stack = []
        word = ''
        # split by space
        for c in s:
            if reading_word:
                if c == SEP:
                    reading_word = False
                    stack.append(word)
                    word = ''
                else:
                    word += c
            else:
                if c != SEP:
                    reading_word = True
                    word += c

        # reverse
        reversed_s = ''
        while stack:
            word = stack.pop()
            if stack:
                reversed_s += word + SEP
            else:
                reversed_s += word
        return reversed_s


s = Solution()
str = ' this is a  good  10 example?'
a = s.reverseWords(str)
print(a)

# @lc code=end
