#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
from typing import List


# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # BFS, generate strings by removing ( or )
        # and keep bfs until we found a valid string

        # no duplicate strings
        candidates = {s}
        found_valid_in_candidates = False
        res = []
        parenthese_set = {'(', ')'}
        # only try to remove parentheses
        # if we haven't found valid str at current removal
        while not found_valid_in_candidates:
            for s in candidates:
                if self.isValid(s):
                    res.append(s)
            # to remove the minimal parentheses
            # once we found a valid string, no need to search any more
            if res:
                found_valid_in_candidates = True
                continue

            next_candidates = set()
            # bfs - try to remove each '(' and ')'
            for s in candidates:
                for i, c in enumerate(s):
                    if c in parenthese_set:
                        # remove parenthese and return substring
                        substring = s[:i] + s[i + 1:]
                        next_candidates.add(substring)
            candidates = next_candidates
        return res

    def isValid(self, s: str) -> bool:
        open_parenthese = 0
        for c in s:
            if c == '(':
                open_parenthese += 1
            elif c == ')':
                open_parenthese -= 1

            # too many close parentheses already
            if open_parenthese < 0:
                return False
        # open = close
        return open_parenthese == 0


# @lc code=end
