#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#
from typing import List


# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return []

        d_logs = []
        l_logs = []
        for log in logs:
            # check last char
            if log[-1].isalpha():
                l_logs.append(log)
            else:
                d_logs.append(log)

        # sort
        l_logs.sort(key=self.sortByBodyThenByHead)
        return l_logs + d_logs

    def sortByBodyThenByHead(self, letterLog: str) -> ():
        # split by first space
        head, body = letterLog.split(' ', 1)
        # then return tuple for sort key
        # tuple => sort by item at 0, 1, 2...
        return (body, head)


# @lc code=end
