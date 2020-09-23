#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#
from typing import List


# @lc code=start
class MyInt:
    def __init__(self, div: int, by: int = 1):
        self.div = div
        self.by = by

    # +
    def __add__(self, other):
        div = self.div * other.by + other.div * self.by
        by = self.by * other.by
        return MyInt(div, by)

    # -
    def __sub__(self, other):
        div = self.div * other.by - other.div * self.by
        by = self.by * other.by
        return MyInt(div, by)

    # *
    def __mul__(self, other):
        div = self.div * other.div
        by = self.by * other.by
        return MyInt(div, by)

    # /
    def __truediv__(self, other):
        div = self.div * other.by
        by = self.by * other.div
        return MyInt(div, by)

    # ==
    def __eq__(self, other):
        return self.div * other.by == self.by * other.div

    # >
    def __gt__(self, other):
        return self.div * other.by > self.by * other.div


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        myNums = [MyInt(n) for n in nums]
        return self.dfs(myNums)

    def dfs(self, nums: List[MyInt]) -> bool:
        size = len(nums)
        if size == 1:
            return nums[0] == MyInt(24)

        # 4 pick 2 numbers
        for i in range(size):
            for j in range(i + 1, size):
                for r in self.allOperations(nums[i], nums[j]):
                    remain = [nums[x] for x in range(size) if x != i and x != j] + [r]
                    if self.dfs(remain):
                        return True
        return False

    def allOperations(self, a: MyInt, b: MyInt) -> List[MyInt]:
        # only positive MyInt
        res = [a + b]
        if a != b:
            res.append(a - b if a > b else b - a)
        res.append(a * b)
        if b != MyInt(0):
            res.append(a / b)
        if a != MyInt(0):
            res.append(b / a)
        return res


s = Solution()
a = s.judgePoint24([1, 2, 1, 2])
print(a)
a = s.judgePoint24([1, 3, 6, 4])
print(a)
a = s.judgePoint24([3, 9, 7, 7])
print(a)

# @lc code=end
