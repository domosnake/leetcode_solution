#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
from typing import List


# @lc code=start
class Number:
    LESS_THAN_20 = [
        '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
        'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
        'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
    ]
    LESS_THAN_100 = [
        '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
        'Eighty', 'Ninety'
    ]
    HUNDRED = ['Hundred']
    LESS_THAN_TRILLION = ['', 'Thousand', 'Million', 'Billion']


class Solution:
    def numberToWords(self, num: int) -> str:
        if num < 0:
            return 'Negative'
        if num == 0:
            return 'Zero'

        words = []
        unit = 0
        while num > 0:
            if num % 1000 != 0:
                words = self.toWords(num % 1000) + [Number.LESS_THAN_TRILLION[unit]] + words
            num //= 1000
            unit += 1

        return ' '.join([word for word in words if word])

    def toWords(self, num: int) -> List[str]:
        if num < 20:
            return [Number.LESS_THAN_20[num]]
        if num < 100:
            tens = [Number.LESS_THAN_100[num // 10]]
            less = self.toWords(num % 10)
            return tens + less
        if num < 1000:
            hundred = [Number.LESS_THAN_20[num // 100]] + Number.HUNDRED
            less = self.toWords(num % 100)
            return hundred + less
        return []


# s = Solution()
# a = s.numberToWords(30)
# print(a)

# @lc code=end
