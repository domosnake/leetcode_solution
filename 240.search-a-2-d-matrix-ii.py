#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):

        # :type matrix: List[List[int]]
        # :type target: int
        # :rtype: bool

        # start from top right
        if not matrix:
            return False
        r = 0
        c = len(matrix[0]) - 1
        while c >= 0 and r < len(matrix):
            cell = matrix[r][c]
            if target == cell:
                return True
            # target can only be found below
            elif target > cell:
                r += 1
            # target can only be found in the left
            elif target < cell:
                c -= 1
        # search the while matrix, no found
        return False


# @lc code=end
