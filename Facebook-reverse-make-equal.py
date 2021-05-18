# Reverse to Make Equal
# Given two arrays A and B of length N,
# determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
# Signature
# bool areTheyEqual(int[] arr_a, int[] arr_b)
# Input
# All integers in array are in the range [0, 1,000,000,000].
# Output
# Return true if B can be made equal to A, return false otherwise.
# Example
# A = [1, 2, 3, 4]
# B = [1, 4, 3, 2]
# output = true
# After reversing the subarray of B from indices 1 to 3, array B will equal array A.


class Solution:
    def are_they_equal(self, array_a, array_b):
        start = 0
        for i in range(len(array_a)):
            if array_a[i] != array_b[i]:
                start = i
                break
        end = len(array_a) - 1
        for i in reversed(range(len(array_a))):
            if array_a[i] != array_b[i]:
                end = i
                break

        for _ in range(start, end + 1):
            if array_a[start] != array_b[end]:
                return False
            start += 1
            end -= 1
        return True


s = Solution()
x = [1, 2, 3, 4, 9, 5, 9]
y = [1, 9, 4, 3, 2, 5, 7]
a = s.are_they_equal(x, y)
print(a)
