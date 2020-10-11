#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#
from typing import List


# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if not paths:
            return ''
        # src -> des
        path_table = {}
        for src, des in paths:
            path_table[src] = des
        return self.dfs(paths[0][0], path_table)

    def dfs(self, city, table) -> str:
        if city not in table:
            return city
        return self.dfs(table[city], table)


# @lc code=end
