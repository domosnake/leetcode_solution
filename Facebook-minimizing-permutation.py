# Minimizing Permutations
# In this problem, you are given an integer N, and a permutation,
# P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N).
# You want to rearrange the elements of the permutation into increasing order,
# repeatedly making the following operation:
# Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
# Your goal is to compute the minimum number of such operations required to
# return the permutation to increasing order.
# Signature
# int minOperations(int[] arr)
# Input
# Array arr is a permutation of all integers from 1 to N, N is between 1 and 8
# Output
# An integer denoting the minimum number of operations required to
# arrange the permutation in increasing order
# Example
# If N = 3, and P = (3, 1, 2), we can do the following operations:
# Select (1, 2) and reverse it: P = (3, 2, 1).
# Select (3, 2, 1) and reverse it: P = (1, 2, 3).
# output = 2
from collections import deque


class Solution:
    def minOperations(self, arr):
        s = ''.join([str(a) for a in arr])
        q = deque()
        q.append(s)
        visited = set()
        visited.add(s)

        target = ''.join([str(i + 1) for i in range(len(arr))])
        moves = 0

        # bfs
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return moves

                # all ways of reversing
                for i in range(len(arr) - 1):
                    for j in range(i + 1, len(arr)):
                        next_p = self.reverse_between(cur, i, j)
                        if next_p not in visited:
                            visited.add(next_p)
                            q.append(next_p)
            moves += 1
        return -1

    def reverse_between(self, s, i, j):
        temp = s[i:j + 1]
        return s[:i] + temp[::-1] + s[j + 1:]


s = Solution()
a = s.minOperations([3, 1, 2])
print(a)
