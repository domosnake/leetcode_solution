#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # brackeys must be in pair to be valid
        # for each type: opens = closes & first open then close
        if len(s) % 2 != 0:
            return False
        opens = {'(', '[', '{'}
        closes = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in opens:
                stack.append(c)
            elif len(stack) == 0 or stack[-1] != closes[c]:
                return False
            else:
                stack.pop()
        return len(stack) == 0


# @lc code=end
