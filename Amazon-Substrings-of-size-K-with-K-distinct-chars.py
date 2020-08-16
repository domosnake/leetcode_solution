from typing import List
from typing import Set

# Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.


class Solution:
    def findAllPremutations(self, s: str, k: int) -> List[str]:
        # edge cases
        if not s or k < 0 or k > len(s):
            return []

        # char to choose from
        char_pool = set()
        for c in s:
            char_pool.add(c)
        # res
        permutations = []
        permutation = []
        self.dfs(permutations, permutation, char_pool, k)
        return permutations

    def dfs(self, permutations: List[str], permutation: List[str], char_pool: Set[str], k: int):
        # base case
        if len(permutation) == k:
            permutations.append(''.join(permutation))
            return

        # search all char
        for c in char_pool:
            permutation.append(c)
            # search other chars
            self.dfs(permutations, permutation, set([i for i in char_pool if i != c]), k)
            # back track
            permutation.pop()

    def findUniqueSubstringWithK(self, s: str, k: int) -> Set[str]:
        # sliding window
        window = []
        # result set
        res = set()
        for i in range(len(s) - k + 1):
            # fill the window
            window = s[i:i+k]
            if window not in res:
                # check distinct char
                if len(window) == len(set(window)):
                    res.add(window)
                    window = []
        return list(res)


s = Solution()
a = s.findUniqueSubstringWithK('abacab', 3)
print(a)

a = s.findUniqueSubstringWithK('awaglknagawunagwkwagl', 4)
print(a)
