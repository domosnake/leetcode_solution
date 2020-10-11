#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#


# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if not sentence or not searchWord:
            return -1
        # return min index
        word = 1
        j = 0
        checking = True
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                word += 1
                j = 0
                checking = True
            else:
                if checking:
                    if searchWord[j] != sentence[i]:
                        checking = False
                    else:
                        j += 1
                        if j >= len(searchWord):
                            return word
        return -1


# s = Solution()
# a = s.isPrefixOfWord('i love eating burger especially cheese burger', 'burg')
# print(a)

# @lc code=end
