#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
from string import digits


# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        # trim leading spaces
        # consider only digits
        # return int.min or int.max when out of the range
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        if not str:
            return 0
        numerical = set(digits)
        numStr = ''
        for c in str:
            # when nums is empty
            if not numStr:
                if c == ' ':
                    continue
                elif c == '-' or c == '+' or c in numerical:
                    numStr += c
                else:
                    return 0
            # when nums has some digits
            else:
                if c not in numerical:
                    break
                else:
                    numStr += c

        if numStr == '' or numStr == '+' or numStr == "-":
            return 0

        negative = False
        if numStr[0] == '-' or numStr[0] == '+':
            negative = numStr[0] == '-'
            numStr = numStr[1:]
        nums = 0
        for i in range(len(numStr) - 1, -1, -1):
            add = int(numStr[i]) * (10 ** (len(numStr) - i - 1))
            if negative:
                if -add < INT_MIN + nums:
                    return INT_MIN
            else:
                if add > INT_MAX - nums:
                    return INT_MAX
            nums += add
        return -nums if negative else nums


# @lc code=end
