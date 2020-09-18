#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'

        res = ''
        stack = []
        for n in num:
            # if cur digit is less than prev digit
            # remove the prev digit
            # e.g. 1234321 k = 3
            # remove 4 , 3,  3
            while stack and k > 0 and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)

        # edge case like 111111
        while k > 0:
            stack.pop()
            k -= 1

        # rebuild new num
        while stack:
            res += stack.pop()

        # remove leading 0s by deleting from end
        res = res.rstrip('0')
        # in case res i empty
        if not res:
            return '0'
        return res[::-1]


# @lc code=end
