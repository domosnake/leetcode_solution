#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#


# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {}
        for c in 'balloon':
            balloon[c] = balloon.get(c, 0) + 1
        for c in text:
            if c in balloon:
                balloon[c] += 1
        # smallest count determines max times
        min_num = float('inf')
        for c, v in balloon.items():
            if c == 'o' or c == 'l':
                min_num = min(min_num, (v // 2) - 1)
            else:
                min_num = min(min_num, v - 1)
        return min_num


# s = Solution()
# a = s.maxNumberOfBalloons('nlaebolko')
# print(a)

# a = s.maxNumberOfBalloons('leetcode')
# print(a)

# @lc code=end
