#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = {'(': ')', '{': '}', '[': ']'}
        close_parentheses = {')', ']', '}'}
        stack = []
        for p in s:
            # open
            if p in open_parentheses:
                stack.append(p)
            # close
            elif p in close_parentheses:
                if not stack:
                    return False
                open_p = stack.pop()
                if open_parentheses[open_p] != p:
                    return False
            # ignore any other characters
            else:
                continue
        if stack:
            return False
        return True


# @lc code=end
