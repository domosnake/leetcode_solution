# Return the nth term of Kbonacci numbers
# Kbonacci numbers are numbers where current number is the sum of previous k numbers
# Assume that first k terms are all 1s.
# Input:    n = 5, k = 2
# Output:   n1 = 1
#           n2 = 1
#           n3 = n1 + n2 = 2
#           n4 = n2 + n3 = 3
#           n5 = n3 + n4 = 5
# Explaination: When k = 2, it's typical fibonacci numbers.
#
# Input:    n = 8, k = 5
# Output:   n6 = n1 + n2 + n3 + n4 + n5 = 5
#           n7 = n2 + n3 + n4 + n5 + n6 = 9
#           n8 = n3 + n4 + n5 + n6 + n7 = 17
# Explaination: When k = 5, current term is the sum of privous 5 terms


class Solution:
    def kbonacci(self, n: int, k: int) -> int:
        if k <= 0 or n <= 0:
            return -1
        if n <= k:
            return 1
        window = [1] * k
        window_sum = k
        # computing from n - k - 1 term
        for _ in range(n - k - 1):
            # add cur term to window
            window.append(window_sum)
            # pop head and compute new term
            window_sum += window_sum - window.pop(0)
        return window_sum


s = Solution()
a = s.kbonacci(5, 2)
print(a)

a = s.kbonacci(8, 5)
print(a)
