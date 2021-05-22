# Above-Average Subarrays
# You are given an array A containing N integers. Your task is to find all subarrays
# whose average sum is greater than the average sum of the remaining array elements.
# You must return the start and end index of each subarray in sorted order.
# A subarray that starts at position L1 and ends at position R1 comes before a subarray that
# starts at L2 and ends at R2 if L1 < L2, or if L1 = L2 and R1 ≤ R2.
# Note that we'll define the average sum of an empty array to be 0, and we'll define the indicies of the array
# (for the purpose of output) to be 1 through N. A subarray that contains a single element will have L1 = R1.
# Signature
# Subarray[] aboveAverageSubarrays(int[] A)
# Input
# 1 ≤ N ≤ 2,000
# 1 ≤ A[i] ≤ 1,000,000
# Output
# A Subarray is an object with two integer fields, left and right, defining the range that a given subarray covers.
# Return a list of all above-average subarrays sorted as explained above.
# Example 1
# A = [3, 4, 2]
# output = [[1, 2], [1, 3], [2, 2]]
# The above-average subarrays are [3, 4], [3, 4, 2], and [4].


class Solution:
    def aboveAverageSubarrays(self, A):
        total = sum(A)
        # track sub sum
        sub = 0
        res = []
        n = len(A)
        for i in range(n):
            for j in range(i, n):
                # sub length
                sub_n = j - i + 1
                # avoid divide by zero
                if sub_n == n:
                    res.append([i + 1, j + 1])
                    continue
                # add sub sum as j moves forward
                sub += A[j]
                # cal sub avg and remaining avg
                sub_avg = sub / sub_n
                avg = (total - sub) / (n - sub_n)
                if sub_avg > avg:
                    res.append([i + 1, j + 1])
            # reset sub sum as i moves forward
            sub = 0

        return res


s = Solution()
a = s.aboveAverageSubarrays([3, 4, 2])
print(a)
