#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        digits = [s for s in str(num)]
        _from = -1
        _to = -1
        max_digit = len(digits) - 1
        for i in reversed(range(len(digits) - 1)):
            d = digits[i]
            if d > digits[max_digit]:
                max_digit = i
            elif d < digits[max_digit]:
                _to = i
                _from = max_digit
        if _to >= 0:
            digits[_to], digits[_from] = digits[_from], digits[_to]
            return int(''.join(digits))
        return num


# s = Solution()
# a = 2736
# print(s.maximumSwap(a))

# @lc code=end
