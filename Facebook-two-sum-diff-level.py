# find 2 nodes that sum up to k, but on the different level
#             12
#            / \
#          2    8
#         / \     \
#        1   6     -2
#           / \    /
#          4   7  13
# return 4, 6
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTwoNodes(self, root, k):
        # val to node list
        lookup = {}
        q = deque()
        q.append(root)

        # bfs tree
        while q:
            backup = []
            for _ in range(len(q)):
                cur = q.popleft()
                # search in lookup
                if k - cur.val in lookup:
                    return [cur, lookup[k - cur.val][0]]

                backup.append(cur)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

            # update lookup
            for n in backup:
                if n.val in lookup:
                    lookup[n.val].append(n)
                else:
                    lookup[n.val] = [n]

        return []


s = Solution()
root = TreeNode(12)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(-2)
root.right.left = TreeNode(13)
a = s.findTwoNodes(root, 10)
print(a[0].val, a[1].val)
