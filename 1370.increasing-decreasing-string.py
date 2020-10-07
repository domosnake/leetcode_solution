#
# @lc app=leetcode id=1370 lang=python3
#
# [1370] Increasing Decreasing String
#


# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        res = ''
        while count:
            for k in sorted(count.keys()):
                res += k
                count[k] -= 1
                if count[k] == 0:
                    del count[k]

            for k in sorted(count.keys(), reverse=True):
                res += k
                count[k] -= 1
                if count[k] == 0:
                    del count[k]

        return res


# @lc code=end
