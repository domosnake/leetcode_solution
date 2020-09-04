#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#
from typing import List, Tuple


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # this is a sorting problem
        # sort the nodes by x, then by y(desc), then by node.val
        nodes_xy = self.traverse(root)
        nodes_xy.sort(key=self.sort_byX_byY_ByVal)
        res = []
        # build result, note that same x should be in same group
        for i in range(len(nodes_xy)):
            if i == 0:
                res.append([nodes_xy[i][0].val])
            else:
                # if x is the same, they should be in same group
                node = nodes_xy[i][0]
                x = nodes_xy[i][1][0]
                pre_x = nodes_xy[i - 1][1][0]
                if x == pre_x:
                    res[-1].append(node.val)
                else:
                    res.append([node.val])
        return res

    def traverse(self, root: TreeNode) -> List[Tuple[TreeNode, Tuple[int, int]]]:
        q = [(root, (0, 0))]
        nodes_xy = []
        # traverse the tree and fill the node list
        while q:
            data = q.pop(0)
            node = data[0]
            x = data[1][0]
            y = data[1][1]
            nodes_xy.append(data)
            if node.left:
                q.append((node.left, (x - 1, y - 1)))
            if node.right:
                q.append((node.right, (x + 1, y - 1)))
        return nodes_xy

    def sort_byX_byY_ByVal(self, data: Tuple[TreeNode, Tuple[int, int]]) -> Tuple[int, int, int]:
        node = data[0]
        x = data[1][0]
        y = data[1][1]
        # then return tuple for sort key
        # tuple => sort by item at 0, 1, 2...
        # sort x in asce
        # sort y in desc
        # sort node.val in asce
        return (x, -y, node.val)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
a = s.verticalTraversal(root)
print(a)


# @lc code=end
