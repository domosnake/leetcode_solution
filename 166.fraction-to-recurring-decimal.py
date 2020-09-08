#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return 'Divide by 0'
        if numerator == 0:
            return '0'
        # some variables
        sign = '-' if (numerator < 0) != (denominator < 0) else ''
        quotient = 0
        remainder = 0
        fraction = ''
        seen = {}
        at = 0
        # quotient and remainder (n // d and n % d)
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        # keep dividing until no remainder or remainder repeating
        while remainder != 0:
            if remainder not in seen:
                seen[remainder] = at
                q, remainder = divmod(remainder * 10, abs(denominator))
                fraction += str(q)
                at += 1
            # remainder repeating, break
            else:
                fraction = fraction[:seen[remainder]] + '(' + fraction[seen[remainder]:] + ')'
                break
        return sign + str(quotient) + ('.' + fraction if fraction != '' else '')


# @lc code=end
