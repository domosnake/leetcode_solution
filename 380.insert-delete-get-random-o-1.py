#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
from random import randint


# @lc code=start
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        do_insert = val not in self.val_to_index
        if do_insert:
            self.list.append(val)
            self.val_to_index[val] = len(self.list) - 1
        return do_insert

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        do_remove = val in self.val_to_index
        if do_remove:
            i = self.val_to_index[val]
            # swap
            self.val_to_index[self.list[-1]] = i
            self.list[-1], self.list[i] = self.list[i], self.list[-1]
            # remove
            self.list.pop()
            self.val_to_index.pop(val)
        return do_remove

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = randint(0, len(self.list) - 1)
        return self.list[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# p1 = obj.insert(0)
# p2 = obj.remove(0)
# p1 = obj.insert(-1)
# p2 = obj.remove(0)
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())
# print(obj.getRandom())

# @lc code=end
