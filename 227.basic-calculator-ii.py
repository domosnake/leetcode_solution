#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#


# @lc code=start
class Solution:
    def __init__(self) -> None:
        self._stack = []
        self._ops = {
            '+': self._add,
            '-': self._sub,
            '*': self._mul,
            '/': self._div
        }

    def calculate(self, s: str) -> int:
        cal = False
        for c in s:
            # space
            if c == ' ':
                continue
            # ops
            elif c in self._ops:
                if cal:
                    self._cal()
                # */
                if c == '*' or c == '/':
                    cal = True
                # +-
                else:
                    cal = False
                    while len(self._stack) >= 3:
                        self._cal()
                self._stack.append(c)
            # num
            else:
                if len(self._stack) == 0:
                    self._stack.append(c)
                elif self._stack[-1] in self._ops:
                    self._stack.append(c)
                else:
                    self._stack[-1] += c

        while len(self._stack) >= 3:
            self._cal()

        return self._stack[0]

    def _cal(self):
        b = int(self._stack.pop())
        op = self._ops[self._stack.pop()]
        a = int(self._stack.pop())
        self._stack.append(op(a, b))

    def _div(self, a, b):
        return a // b

    def _mul(self, a, b):
        return a * b

    def _sub(self, a, b):
        return a - b

    def _add(self, a, b):
        return a + b


# s = Solution()
# a = "1-1+1"
# print(s.calculate(a))

# @lc code=end
