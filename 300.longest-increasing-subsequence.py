#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List


# @lc code=start
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 纸牌接龙算法，升序单独放一堆，小的牌放最左边的堆
        #
        # 堆的数量就是最长升序长度
        # 最高的堆就是最长的降序长度
        # 用dfs可以找到所有最长升序
        #
        # patience sort: buckets/piles + binary search
        # O(nlogn)
        nodes = [Node(n) for n in nums]
        piles = []

        for node in nodes:
            n = node.value
            i = 0
            j = len(piles)
            # find the pile to add n
            while i != j:
                mid = (i + j) // 2
                # 比较堆顶的一张
                if piles[mid][-1].value < n:
                    i = mid + 1
                else:
                    j = mid
            # n is the max number, thus add a new pile
            if i == len(piles):
                piles.append([node])
            # add onto a pile
            else:
                piles[i].append(node)
            # set up pointer
            if i > 0:
                for h in reversed(range(len(piles[i - 1]))):
                    if node.value > piles[i - 1][h].value:
                        node.children.append(piles[i - 1][h])
                    else:
                        break

        length_of_LIS = self._lengthOfLIS(piles)
        paths_of_LIS = self._pathsOfLIS(piles)
        length_of_LDS = self._lengthOfLDS(piles)
        paths_of_LDS = self._pathsOfLDS(piles)

        print(f'Longest Increasing Subsequences: {paths_of_LIS}')
        print(f'LIS length: {length_of_LIS}')
        print('-----------------------------')
        print(f'Longest Decreasing Subsequences: {paths_of_LDS}')
        print(f'LDS length: {length_of_LDS}')
        #
        # Longest Increasing Subsequences: [[2, 3, 7, 101], [2, 5, 7, 101], [2, 3, 7, 18], [2, 5, 7, 18]]
        # LIS length: 4
        # -----------------------------
        # Longest Decreasing Subsequences: [[10, 9, 2]]
        # LDS length: 3
        #
        return length_of_LIS

    def _lengthOfLIS(self, piles):
        return len(piles)

    def _pathsOfLIS(self, piles):
        paths = []
        for node in piles[-1]:
            self._dfs(node, [node.value], paths)
        return paths

    def _dfs(self, node, path, paths):
        if len(node.children) == 0:
            paths.append(path[::-1])
            return

        for child in node.children:
            path.append(child.value)
            self._dfs(child, path, paths)
            # backtrack
            path.pop()

    def _lengthOfLDS(self, piles):
        maxLen = 0
        for pile in piles:
            maxLen = max(maxLen, len(pile))
        return maxLen

    def _pathsOfLDS(self, piles):
        lengOfLDS = self._lengthOfLDS(piles)
        paths = [[node.value for node in pile] for pile in piles
                 if len(pile) == lengOfLDS]
        return paths


# test
s = Solution()
a = [10, 9, 2, 5, 3, 7, 101, 18]
s.lengthOfLIS(a)

# @lc code=end
