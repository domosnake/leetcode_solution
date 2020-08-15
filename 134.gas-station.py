#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
from typing import List


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # net gas at each station
        net_gas = [i - j for i, j in zip(gas, cost)]
        # not possbie if total net gas is negative
        if sum(net_gas) < 0:
            return -1
        start = 0
        tank = 0
        # why do we only need one pass to find the anwser?
        # say you start from A and you strand at B
        # then you know your tank has gas until B
        # thus, starting anywhere beyond A will result less gas in tank
        # furthermore, you must start some point beyond B
        for i in range(len(net_gas)):
            tank += net_gas[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start


# @lc code=end
