# Given a string array representing a throw ball blocks,
# each string is either a number or +, Z, X.
# Calculate total.
# If number, just add to total.
# If +, add last 2 scores to total.
# If Z, remove last score from total.
# If X, double last score and add to total.
#
# Use 0 for any missing last score

from typing import List


class Solution:
    def calculateBaseballScore(self, score: List[str]) -> int:
        # stack
        # edge case, all '+'
        stack = [0] * 2 * len(score)
        for s in score:
            if s == '+':
                last = stack[-1]
                prevLast = stack[-2]
                stack.append(last + prevLast)
            elif s == 'Z':
                stack.pop()
            elif s == 'X':
                last = stack[-1]
                stack.append(last * 2)
            else:
                # check if the scors can be converted to int
                try:
                    stack.append(int(s))
                except ValueError:
                    continue
        return sum(stack)


s = Solution()
score = ["Z", "Z", "Z", "Z", "+", "+", "X", "-"]
a = s.calculateBaseballScore(score)
print(a)
