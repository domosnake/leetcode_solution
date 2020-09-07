#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
from typing import List
from random import randint


# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        copy = self.original[:]
        length = len(copy)
        for i in range(length):
            # some random index to swap with
            swapWith = randint(0, length - 1)
            # swap
            copy[i], copy[swapWith] = copy[swapWith], copy[i]
        return copy

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
