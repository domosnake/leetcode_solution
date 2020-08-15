#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
from typing import Dict


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        # dfs recursively
        copy = Node(val=node.val)
        visited = {node: copy}
        self.dfs_copy(node, visited)
        return copy

    def dfs_copy(self, parent: Node, visited: Dict) -> None:
        for child in parent.neighbors:
            if child not in visited:
                child_copy = Node(val=child.val)
                visited[child] = child_copy
                # add child copy to parent copy
                visited[parent].neighbors.append(visited[child])
                # keep copying
                self.dfs_copy(child, visited)
            else:
                # add child copy to parent copy
                visited[parent].neighbors.append(visited[child])


# @lc code=end
