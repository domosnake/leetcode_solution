#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
from typing import List


# @lc code=start
class TrieNode:
    def __init__(self):
        self.is_key = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_key = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # to avoid searching prefix repetitively
        # we can use prefix tree - trie
        if not board or not words:
            return []

        trie = Trie()
        for word in words:
            trie.insert(word)

        res = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.trie_dfs(trie.root, '', board, r, c, res)
        return list(res)

    def trie_dfs(self, node, word, board, r, c, res):
        if node.is_key:
            res.add(word)
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return
        if board[r][c] not in node.children:
            return

        node = node.children[board[r][c]]
        char = board[r][c]
        board[r][c] = '$'

        self.trie_dfs(node, word + char, board, r, c - 1, res)
        self.trie_dfs(node, word + char, board, r, c + 1, res)
        self.trie_dfs(node, word + char, board, r - 1, c, res)
        self.trie_dfs(node, word + char, board, r + 1, c, res)

        board[r][c] = char

    def findWords_dfs(self, board: List[List[str]], words: List[str]) -> List[str]:
        # the main issue of brute force dfs solution is that
        # it may have a lot of redundant searches
        # for instance, to search 'apple', we will do dfs once, and say the word is found
        # to search the next word 'applepie', we need to dfs again from the fitst char
        # which is redundant, instead, we could have searched 'pie' directly since 'apple' is found
        if not board or not words:
            return []

        letter_set = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                letter_set.add(board[r][c])

        words_found = []
        for word in words:
            if not set(word).issubset(letter_set):
                continue
            # dfs the word in board
            found = False
            for r in range(len(board)):
                for c in range(len(board[0])):
                    found = self.dfs(word, 0, board, r, c)
                    if found:
                        words_found.append(word)
                        break
                if found:
                    break
        return words_found

    def dfs(self, word, at, board, r, c) -> bool:
        # base cases
        if not (0 <= r < len(board) and 0 <= c < len(board[0])):
            return False
        if board[r][c] != word[at]:
            return False
        if at == len(word) - 1 and board[r][c] == word[at]:
            return True

        board[r][c] = '$'
        found = self.dfs(word, at + 1, board, r, c - 1) or \
            self.dfs(word, at + 1, board, r, c + 1) or \
            self.dfs(word, at + 1, board, r - 1, c) or \
            self.dfs(word, at + 1, board, r + 1, c)

        board[r][c] = word[at]
        return found


# s = Solution()
# board = [['o', 'a', 'a', 'n'],
#          ['e', 't', 'a', 'e'],
#          ['i', 'h', 'k', 'r'],
#          ['i', 'f', 'l', 'v']]
# a = s.findWords(board, ["oath", "pea", "eat", "rain"])
# print(a)

# @lc code=end
