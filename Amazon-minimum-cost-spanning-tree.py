# Given a list of weighted edges between nodes, find the minimum cost spanning tree.
from typing import List


class Solution:
    def weightOfMST(self, nodes: List[str], repetitions: bool) -> int:
        # basicall, given a weighted, connected and undirected graph
        # we are to find the weight of minimum spanning tree(s)
        # note that such graph can have more than one minimum spanning tree
        #
        # greedy
        # always pick the edge with min weight
        