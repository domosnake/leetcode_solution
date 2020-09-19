# Finding the intersection of two lists of strings.
from typing import List


class Solution:
    def intersect(self, aList: List[str], bList: List[str], repetitions: bool) -> List[str]:
        common = []
        counter = {}
        # count strings in a
        for a in aList:
            counter[a] = counter.get(a, 0) + 1
        # decreament count when a == b
        for b in bList:
            # a == b and we have positive number of a to decreament
            if b in counter and counter[b] > 0:
                common.append(b)
                # show repetitions as many times as they show in both lists
                if repetitions:
                    counter[b] -= 1
                # show unique elements
                else:
                    counter[b] = -1
        return common


s = Solution()
aList = ['qwe', 'zxc', 'zxc', 'qwe', 'qwe', 'tyu', 'bnm', 'uio', 'qwe', 'hjk', 'asd', 'asd']
bList = ['qwe', 'zxc', 'tyu', 'bnm', 'asd', 'asd']
a = s.intersect(aList, bList, repetitions=True)
print(a)
a = s.intersect(aList, bList, repetitions=False)
print(a)
