# Input: codeList = [[apple, apple], [banana, anything, banana]]
# shoppingCart = [orange, apple, apple, banana, orange, banana]
# result: 1
from typing import List

# Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits.
# The combination will change each day,
# and the team running the promotion wants to use a code list to make it easy to change the combination.
# The code list contains groups of fruits.
# Both the order of the groups within the code list and the order of the fruits within the groups matter.
# However, between the groups of fruits, any number, and type of fruit is allowable.
# The term "anything" is used to allow for any type of fruit to appear in that location within the group.
# Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
# Based on the above secret code list, a customer who made either of the following purchases would win the prize:
# orange, apple, apple, banana, orange, banana
# apple, apple, orange, orange, banana, apple, banana, banana
# Write an algorithm to output 1 if the customer is a winner else output 0.

# Input
# The input to the function/method consists of two arguments:
# codeList, a list of lists of strings representing the order and
# grouping of specific fruits that must be purchased in order to win the prize for the day.
# shoppingCart, a list of strings representing the order in which a customer purchases fruit.
# Output
# Return an integer 1 if the customer is a winner else return 0.
# Note
# 'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group.
# 'anything' has to be something, it cannot be "nothing."
# 'anything' must represent one and only one fruit.
# If secret code list is empty then it is assumed that the customer is a winner.


class Solution:
    def winPrize(self, codeList: List[List[str]],
                 shoppingCart: List[str]) -> int:
        if not shoppingCart:
            return 0
        # sliding window
        # code
        i = 0
        # shopping cart
        j = 0

        while i < len(shoppingCart):
            # all codes match before shopping cart ends
            if j >= len(codeList):
                return 1
            window = codeList[j]
            match = self.matchWindow(window, shoppingCart, i)
            if not match:
                i += 1
            else:
                j += 1
                # slide i by length of window
                i += len(window)
        # all codes match and shopping cart ends
        if j >= len(codeList):
            return 1
        # shoping cart ends, but not all codes match
        return 0

    def matchWindow(self, window: List[str], shoppingCart: List[str],
                    at: int) -> bool:
        for i in range(len(window)):
            if at + i < len(shoppingCart):
                if window[i] == 'anything':
                    continue
                if window[i] != shoppingCart[at + i]:
                    return False
        return True


s = Solution()
codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"]
a = s.winPrize(codeList, shoppingCart)
print(a)

codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["banana", "orange", "banana", "apple", "apple"]
a = s.winPrize(codeList, shoppingCart)
print(a)

codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["apple", "banana", "apple", "banana", "orange", "banana"]
a = s.winPrize(codeList, shoppingCart)
print(a)

codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["apple", "apple", "apple", "banana", "apple", "banana"]
a = s.winPrize(codeList, shoppingCart)
print(a)

codeList = [["anything", "anything", "anything", "apple"],
            ["banana", "anything", "banana"]]
shoppingCart = [
    "orange", "orange", "orange", "orange", "apple", "orange", "orange",
    "banana", "orange", "banana"
]
a = s.winPrize(codeList, shoppingCart)
print(a)
