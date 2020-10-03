#
# @lc app=leetcode id=1175 lang=python3
#
# [1175] Prime Arrangements
#
from math import factorial


# @lc code=start
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # permutations of 1 to n = factorail(n)
        # for example n = 3:
        # [1, 2, 3]
        # [1, 3, 2]
        # [2, 1, 3]
        # [2, 3, 1]
        # [3, 1, 2]
        # [3, 2, 1]
        primes_count = 0
        for i in range(n):
            if self.isPrime(i+1):
                primes_count += 1
        # prime can be freely arranged at prime index
        prime_arrangement = factorial(primes_count)
        # non-prime can be freely arranged at non-prime index
        non_prime_arrangement = factorial(n - primes_count)
        return (prime_arrangement * non_prime_arrangement) % (10**9 + 7)

    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


# s = Solution()
# a = s.numPrimeArrangements(2)
# print(a)

# @lc code=end
