#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#


# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = '(' + s + ')'
        # track parentheses
        stack = []
        number = 0
        result = 0
        sign = 1
        for c in s:
            # current number
            if c.isdigit():
                number = (number * 10) + int(c)

            elif c == '+':
                result += (sign * number)
                # reset for the next number
                number = 0
                sign = 1

            elif c == '-':
                result += (sign * number)
                # reset for the next number
                number = 0
                sign = -1

            elif c == '(':
                # push result
                stack.append(result)
                # push sign
                stack.append(sign)
                result = 0
                sign = 1

            elif c == ')':
                result += (sign * number)
                number = 0
                # pop sign
                result *= stack.pop()
                # pop result
                result += stack.pop()

            # skip spaces
            else:
                continue

        return result


# s = Solution()
# str = ' (1 + (4 +5+2)- 3) +( 6+8)'
# a = s.calculate(str)
# print(a)

# @lc code=end
