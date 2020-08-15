from typing import List

# Given 2 lists a and b.
# Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value.
# Your task is to find an element from a and an element form b
# such that the sum of their values is less or equal to target and as close to target as possible.
# Return a list of ids of selected elements. If no pair is possible, return an empty list.


class Solution:
    def optimalUtilization(self, a: List[List[int]], b: List[List[int]], target: int) -> List[List[int]]:
        ids = []
        max_sum = float('-inf')
        for a_id, a_val in a:
            for b_id, b_val in b:
                cur_sum = a_val + b_val
                if cur_sum <= target:
                    if cur_sum > max_sum:
                        ids = [[a_id, b_id]]
                        max_sum = cur_sum
                    elif cur_sum == max_sum:
                        ids.append([a_id, a_id])
        return ids


s = Solution()

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
x = s.optimalUtilization(a, b, target)
print(x)

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
x = s.optimalUtilization(a, b, target)
print(x)

a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
x = s.optimalUtilization(a, b, target)
print(x)

a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
x = s.optimalUtilization(a, b, target)
print(x)

a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = -12
x = s.optimalUtilization(a, b, target)
print(x)
