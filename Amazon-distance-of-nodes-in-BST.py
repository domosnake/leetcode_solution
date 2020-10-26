from typing import List

# Given a list of unique integers nums,
# construct a BST from it (you need to insert nodes one-by-one with the given order to get the BST)
# and find the distance between two nodes node1 and node2.
# Distance is the number of edges between two nodes.
# If any of the given nodes does not appear in the BST, return -1.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        cur = root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
        return root

    def lowestCommonAncestorInBST(self, root: TreeNode, node1: int, node2: int) -> TreeNode:
        if root is None:
            return None
        node = root
        while node:
            # left sub tree
            if node1 < node.val and node2 < node.val:
                node = node.left
            # right sub tree
            elif node1 > node.val and node2 > node.val:
                node = node.right
            # node1 and node2 on diff sub tree
            else:
                return node

    def distanceToAncestorInBST(self, ancestor: TreeNode, node: int) -> int:
        if ancestor is None:
            return -1
        cur = ancestor
        distance = 0
        while cur:
            if node < cur.val:
                distance += 1
                cur = cur.left
            elif node > cur.val:
                distance += 1
                cur = cur.right
            else:
                return distance

    def distanceBetweenNodesInBST(self, nums: List[int], node1: int, node2: int) -> int:
        # build bst
        treeSet = set()
        root = None
        for n in nums:
            root = self.insertIntoBST(root, n)
            treeSet.add(n)

        if node1 not in treeSet or node2 not in treeSet:
            return -1
        # find lowest common ancestor
        ancestor = self.lowestCommonAncestorInBST(root, node1, node2)
        node1_to_ancestor = self.distanceToAncestorInBST(ancestor, node1)
        node2_to_ancestor = self.distanceToAncestorInBST(ancestor, node2)
        return node1_to_ancestor + node2_to_ancestor


s = Solution()

a = s.distanceBetweenNodesInBST([2, 1, 3], 3, 1)
print(a)

a = s.distanceBetweenNodesInBST(
    [99, 65, 38, 100, 25, 78, 3, 7, 5, 1, 8, 9, 11, 38, 74], 25, 7)
print(a)

a = s.distanceBetweenNodesInBST(
    [99, 65, 38, 100, 25, 78, 3, 7, 5, 1, 8, 9, 11, 38, 74], 100, 11)
print(a)
