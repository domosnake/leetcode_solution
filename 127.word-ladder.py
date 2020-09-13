#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
from typing import List
from string import ascii_lowercase


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bidirectional bfs
        words = set(wordList)
        if endWord not in words:
            return 0

        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        ladder = 1
        alpha = ascii_lowercase
        while beginSet:
            ladder += 1
            # put new words in this temp set
            temp = set()
            for word in beginSet:
                # for each char in word, change to new char
                # see if we can find in endSet
                for i in range(len(word)):
                    for c in alpha:
                        # slice word to get new word
                        new_word = word[:i]+c+word[i+1:]
                        if new_word in endSet:
                            return ladder
                        if new_word in words and new_word not in visited:
                            temp.add(new_word)
                            visited.add(new_word)
            beginSet = temp
            # swap for better performance
            # also move endSet towards beginSet
            # thus bidirectional bfs
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
        return 0


# @lc code=end
