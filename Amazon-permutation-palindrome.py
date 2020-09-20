# Given a string, determine if a permutation of the string could form a palindrome.
# Input: "code"
# Output: false
#
# Input: "aab"
# Output: true
#
# Input: "carerac"
# Output: true
class Solution:
    def canFormPalindrome(self, s: str) -> bool:
        counter = {}
        # count char frequency
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        # many odd char we have in the string
        oddCharNum = 0
        for char in counter:
            if counter[char] % 2 != 0:
                oddCharNum += 1
            # more than 1 odd char, can not from palindrome
            if oddCharNum > 1:
                return False
        # odd char num should only 0 or 1
        return True

    def canFormPalindrome_set(self, s: str) -> bool:
        charSet = set()
        for char in s:
            if char in charSet:
                charSet.discard(char)
            else:
                charSet.add(char)
        # if palindrome
        # in the end, the set should only have 0 or 1 char
        # because even char are canceled out
        if len(charSet) <= 1:
            return True
        else:
            return False


s = Solution()
a = s.canFormPalindrome('code')
print(a)
a = s.canFormPalindrome('amazon')
print(a)
a = s.canFormPalindrome('racecar')
print(a)
a = s.canFormPalindrome('1234123')
print(a)
a = s.canFormPalindrome('12341235')
print(a)
