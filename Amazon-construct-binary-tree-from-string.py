# You need to construct a binary tree
# from a string consisting of parenthesis and integers
#
# The whole input represents a binary tree
# It contains an integer followed by zero, one or two pairs of parenthesis
# The integer represents the root's value
# and a pair of parenthesis contains a child binary tree with the same structure
#
# You always start to construct the left child node of the parent first if it exists.
#
# Example:
#
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
#
# Note:
#
# There will only be '(', ')', '-' and '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # use stack
        if not s:
            return None
        parentStr = self.extractParentStr(s)
        parent = TreeNode(int(parentStr))
        childrenStr = self.extractChildrenStr(s)
        # recursively build subtrees
        if childrenStr:
            parent.left = self.str2tree(childrenStr[0])
            parent.right = self.str2tree(childrenStr[1])
        return parent

    def extractParentStr(self, s: str) -> str:
        # input: 4(2(3)(1))(6(5))
        # output: 4
        #
        # input: 2(3)(1)
        # output: 2
        #
        # input: 3
        # output: 3 (no children)
        if not s:
            return None
        first_open_parenthesis = s.find('(')
        # no children
        if first_open_parenthesis == -1:
            return s
        return s[:first_open_parenthesis]

    def extractChildrenStr(self, s: str) -> (str, str):
        # input: 4(2(3)(1))(6(5))
        # output: 2(3)(1) for left, and 6(5) for right
        #
        # input: 2(3)(1)
        # output: 3 for left, and 1 for right
        #
        # input: 6(5)
        # output: 5 for left, and '' for right
        #
        # input: 2
        # output: None (no children)
        if not s:
            return None
        first_open_parenthesis = s.find('(')
        # no children
        if first_open_parenthesis == -1:
            return None
        stack = ['(']
        leftEnd = first_open_parenthesis + 1
        leftStart = leftEnd
        while stack:
            if s[leftEnd] == '(':
                stack.append(s[leftEnd])
            elif s[leftEnd] == ')':
                stack.pop()
            leftEnd += 1
        # str of left subtree = x(y)(z)
        left = s[leftStart: leftEnd - 1]
        # str of right subtree = x(y)(z)
        right = s[leftEnd + 1: -1]
        return (left, right)


s = Solution()
a = s.str2tree("4(2(3)(1))(6(5))")
print(a)
