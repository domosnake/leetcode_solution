from typing import List
from heapq import heapify, heappop, heappush

# Given n ropes of different lengths, we need to connect these ropes into one rope.
# We can connect only 2 ropes at a time.
# The cost required to connect 2 ropes is equal to sum of their lengths.
# The length of this connected rope is also equal to the sum of their lengths.
# This process is repeated until n ropes are connected into a single rope.
# Find the min possible cost required to connect all ropes.
#
# Example 1:
#
# Input: ropes = [8, 4, 6, 12]
# Output: 58
# Explanation: The optimal way to connect ropes is as follows
# 1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
# 2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
# 3. Connect the ropes of length 18 and 12 (cost is 30).
# Total cost to connect the ropes is 10 + 18 + 30 = 58


class Solution:
    def minCostToConnectRopes(self, ropes: List[int]) -> int:
        # min heap
        heapify(ropes)
        total = 0
        while len(ropes) > 1:
            # connect 2 shorest ropes
            new_rope = heappop(ropes) + heappop(ropes)
            total += new_rope
            # add new rope back to heap
            heappush(ropes, new_rope)
        return total


s = Solution()

ropes = [8, 4, 6, 12]
x = s.minCostToConnectRopes(ropes)
print(x)

ropes = [20, 4, 8, 2]
x = s.minCostToConnectRopes(ropes)
print(x)

ropes = [1, 2, 5, 10, 35, 89]
x = s.minCostToConnectRopes(ropes)
print(x)

ropes = [2, 2, 3, 3]
x = s.minCostToConnectRopes(ropes)
print(x)
