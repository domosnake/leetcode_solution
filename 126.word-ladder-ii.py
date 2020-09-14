#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # bidirectional bfs
        words = set([beginWord] + wordList)
        if endWord not in words:
            return []

        alpha = set(''.join(words))
        searchBegin = {beginWord}
        searchEnd = {endWord}
        searchForward = True
        stopSearch = False
        visited = set([beginWord, endWord])

        connectTo = defaultdict(set)
        connectToBack = defaultdict(set)

        while searchBegin:
            # put new words in this temp set
            temp = set()
            for word in searchBegin:
                # for each char in word, change to new char
                # see if we can find in searchEnd
                for i in range(len(word)):
                    for c in alpha:
                        # slice word to get new word
                        new_word = word[:i]+c+word[i+1:]
                        if new_word in words:
                            if new_word in searchEnd:
                                stopSearch = True
                                if searchForward:
                                    connectTo[word].add(new_word)
                                else:
                                    connectToBack[new_word].add(word)
                            if new_word not in visited:
                                temp.add(new_word)
                                visited.add(new_word)
                                if searchForward:
                                    connectTo[word].add(new_word)
                                else:
                                    connectToBack[new_word].add(word)
            if stopSearch:
                break

            searchBegin = temp
            # swap for better performance
            # also move searchEnd towards searchBegin
            # thus bidirectional bfs
            if len(searchBegin) > len(searchEnd):
                searchForward = not searchForward
                searchBegin, searchEnd = searchEnd, searchBegin

        # dfs all paths
        paths = []
        path = [beginWord]
        connectTo.update(connectToBack)
        self.dfs(beginWord, endWord, connectTo, path, paths)

        return paths

    def findLadders_form_word_graph(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
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
        graph = self.buildGraph(words)

        # store the predecessor(s) of a given word while doing bfs
        # use connectTo to form path graph, directed unweighted graph
        connectTo = {w: set() for w in words}

        # distance from the begin word
        # use distance to avoid paths longer than shortest distance from begin to end
        # also use distance to avoid cycles
        distance = {w: float('inf') for w in words}

        # bfs
        self.bfs(graph, beginWord, endWord, connectTo, distance)

        # now all our paths can be extracted from connectTo via dfs
        paths = []
        path = [beginWord]
        self.dfs(beginWord, endWord, connectTo, path, paths)

        return paths

    def buildGraph(self, words: set) -> {str: set}:
        graph = {}
        for a in words:
            adjacency = set()
            for b in words:
                # a is connected to b only their diff is 1
                if self.diff(a, b) == 1:
                    adjacency.add(b)
            graph[a] = adjacency
        return graph

    def dfs(self, begin: str, end: str, connectTo: {str: set}, path: List[str], paths: List[List[str]]):
        # base
        if begin == end:
            # save copied path
            paths.append(path[:])
            return
        # for each connected words
        for to in connectTo[begin]:
            # add to path
            path.append(to)
            # keep dfs
            self.dfs(to, end, connectTo, path, paths)
            # backtrack
            path.pop()

    def bfs(self, graph: {str: set}, begin: str, end: str, connectTo: {str: set}, distance: {str: int}):

        # queue for bfs
        q = [begin]
        distance[begin] = 0

        # bfs
        while q:
            cur = q.pop(0)
            # no need to explore longer path
            if distance[cur] >= distance[end]:
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

    def diff(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return -1
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
        return diff


s = Solution()
x = "magic"
y = "pearl"
z = ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth","yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch","basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan","foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks","dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty","slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled","acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic","luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks","demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole","suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile","orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge","molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny","pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx","maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy","decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars","robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]
a = s.findLadders(x, y, z)
# [["magic","manic","mania","maria","marta","marty","party","parry","perry","peary","pearl"],["magic","manic","mania","maria","maris","paris","parks","perks","peaks","pears","pearl"],["magic","manic","mania","maria","marta","marty","marry","merry","perry","peary","pearl"],["magic","manic","mania","maria","marta","marty","marry","parry","perry","peary","pearl"],["magic","manic","mania","maria","maris","marks","parks","perks","peaks","pears","pearl"]]
print(a)

# @lc code=end
