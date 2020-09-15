#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List, Dict, Set
from collections import defaultdict


# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # bidirectional bfs + dfs
        words = set([beginWord] + wordList)
        if endWord not in words:
            return []

        chars = set(''.join(words))
        searchBegin = {beginWord}
        searchEnd = {endWord}
        bfs_forward = True
        stopSearch = False

        # distance from begin or end, used to avoid going in circles
        dist_front = defaultdict(lambda: float('inf'))
        dist_back = defaultdict(lambda: float('inf'))
        dist_front[beginWord] = 0
        dist_back[endWord] = 0
        # build path graph for bfs in both directions
        paths_front = defaultdict(set)
        paths_back = defaultdict(set)

        # bfs
        while searchBegin:
            # put new words in this temp set
            temp = set()
            for word in searchBegin:
                # for each char in word, change to new char
                # see if we can find in searchEnd
                for i in range(len(word)):
                    for c in chars:
                        # slice word to get a new word
                        new_word = word[:i]+c+word[i+1:]
                        # cases to skip the word
                        # case 1: same word
                        if new_word == word:
                            continue
                        # case 2: word not in original word list
                        if new_word not in words:
                            continue
                        # case 3: going in circles
                        if bfs_forward:
                            if dist_front[new_word] <= dist_front[word]:
                                continue
                        else:
                            if dist_back[new_word] <= dist_back[word]:
                                continue
                        # find a shorest path
                        if new_word in searchEnd:
                            stopSearch = True
                        else:
                            temp.add(new_word)
                        # update path and distance
                        if bfs_forward:
                            paths_front[word].add(new_word)
                            dist_front[new_word] = dist_front[word] + 1
                        else:
                            paths_back[new_word].add(word)
                            dist_back[new_word] = dist_back[word] + 1
            # all words from searchBegin are explored
            # if this flag is true, it means all shortest paths are found
            # no need to explore further
            if stopSearch:
                break

            searchBegin = temp
            # change dfs direction for better performance
            # only search from smaller set to reduce search universe
            if len(searchBegin) > len(searchEnd):
                bfs_forward = not bfs_forward
                searchBegin, searchEnd = searchEnd, searchBegin

        # dfs all paths
        paths = []
        path = [beginWord]
        # merge to form paths from begin to end
        paths_front.update(paths_back)
        self.dfs(beginWord, endWord, paths_front, path, paths)

        return paths

    def findLadders_via_word_graph(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # this problem is a graph problem solved by dfs and bfs
        # 1. realize that word list, incluing begin word, can be viewed a word graph
        #    where words are connected if their diff is 1
        #    for instance, "hit" is connected to "hot", "xy" is not connected to "ab"
        # 2. bfs the word graph to form another path graph
        #    the path graph contains only shorest paths from begin word to end word
        # 3. dfs the path graph to extract all paths
        words = set([beginWord] + wordList)
        if endWord not in words:
            return []

        # build graph, bi-directed unweighted graph of all words
        graph = {}
        for a in words:
            adjacency = set()
            for b in words:
                # a is connected to b only iftheir diff is 1
                diff = 0
                for i in range(len(a)):
                    if a[i] != b[i]:
                        diff += 1
                if diff == 1:
                    adjacency.add(b)
            graph[a] = adjacency

        # store the predecessor(s) of a given word while doing bfs
        # use connectTo to form path graph, directed unweighted graph
        connectTo = defaultdict(set)

        # distance from the begin word
        # use distance to avoid paths longer than shortest distance from begin to end
        # also use distance to avoid cycles
        distance = defaultdict(lambda: float('inf'))
        distance[beginWord] = 0

        # bfs
        # queue for bfs
        q = [beginWord]
        while q:
            cur = q.pop(0)
            # no need to explore longer path
            if distance[cur] >= distance[endWord]:
                # block the way by NOT adding it's adj to queue
                continue
            # explore adjacent words
            for adj in graph[cur]:
                # avoid cycle, only moving forward
                # adj's distance should be larger than cur's
                if distance[adj] <= distance[cur]:
                    continue
                # update distance
                distance[adj] = distance[cur] + 1
                # update connectTo, cur -> adj
                connectTo[cur].add(adj)
                # add adj to queue
                q.append(adj)

        # now all our paths can be extracted from connectTo via dfs
        paths = []
        path = [beginWord]
        self.dfs(beginWord, endWord, connectTo, path, paths)

        return paths

    def dfs(self, begin: str, end: str, graph: Dict[str, Set[str]], path: List[str], paths: List[List[str]]):
        # base
        if begin == end:
            # save copied path
            paths.append(path[:])
            return
        # for each connected words
        for to in graph[begin]:
            # add to path
            path.append(to)
            # keep dfs
            self.dfs(to, end, graph, path, paths)
            # backtrack
            path.pop()


# @lc code=end
