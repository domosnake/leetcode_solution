# Nodes in a Subtree
# You are given a tree that contains N nodes,
# each containing an integer u which corresponds to
# a lowercase character c in the string s using 1-based indexing.
# You are required to answer Q queries of type [u, c],
# where u is an integer and c is a lowercase letter.
# The query result is the number of nodes in the subtree of node u containing c.
#
# Signature
# int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
# Input
# A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
# Constraints
# N and Q are the integers between 1 and 1,000,000
# u is a unique integer between 1 and N
# s is of the length of N, containing only lowercase letters
# c is a lowercase letter contained in string s
# Node 1 is the root of the tree
# Output
# An integer array containing the response to each query
# Example
#         1(a)
#         /   \
#       2(b)  3(a)
# s = "aba"
# RootNode = 1
# query = [[1, 'a']]
# Note: Node 1 corresponds to first letter 'a',
# Node 2 corresponds to second letter of the string 'b',
# Node 3 corresponds to third letter of the string 'a'.
# output = [2]
# Both Node 1 and Node 3 contain 'a',
# so the number of nodes within the subtree of Node 1 containing 'a' is 2.


class Node:
    def __init__(self, data):
        self.val = data
        self.children = []


class Solution:
    def count_of_nodes(self, root, queries, s):
        dp = {}
        set_s = set(s)
        for i in range(len(s)):
            nodes = {c: 0 for c in set_s}
            dp[i + 1] = nodes

        # update dp for all node and all char
        self._dfs(root, s, set_s, dp)

        # query result
        res = []
        for q in queries:
            # no such node
            if q[0] not in dp:
                res.append(0)
                continue

            # no such char
            if q[1] not in dp[q[0]]:
                res.append(0)
                continue

            res.append(dp[q[0]][q[1]])

        return res

    def _dfs(self, node, s, set_s, dp):
        # update dp for the node itself
        for c in set_s:
            if s[node.val - 1] == c:
                dp[node.val][c] += 1

        # if it has subtrees
        for child in node.children:
            self._dfs(child, s, set_s, dp)
            # update dp for its subtrees
            for c in set_s:
                dp[node.val][c] += dp[child.val][c]


s = Solution()
ss = 'abaacab'
root = Node(1)
root.children.append(Node(2))
root.children.append(Node(3))
root.children.append(Node(7))
root.children[0].children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[1].children.append(Node(6))
queries = [(1, 'a'), (2, 'b'), (3, 'a')]

a = s.count_of_nodes(root, queries, ss)
print(a)
