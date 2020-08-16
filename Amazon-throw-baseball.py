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
                last = stack.pop()
                prevLast = stack.pop()
                stack.append(last + prevLast)
            elif s == 'Z':
                stack.pop()
            elif s == 'X':
                last = stack.pop()
                stack.append(last * 2)
            else:
                stack.append(int(s))
        return sum(stack)


s = Solution()
score = ["5", "-2", "4", "Z", "X", "9", "+", "+"];
a = s.calculateBaseballScore(score)
print(a)
