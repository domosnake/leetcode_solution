#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#


# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            xor ^= start + 2 * i
        return xor


# @lc code=end
