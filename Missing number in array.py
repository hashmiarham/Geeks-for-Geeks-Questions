#User function Template for python3


class Solution:
    def missingNumber(self,array, n):
        total_sum = n * (n + 1) // 2  # calculate sum of integers from 1 to N
        array_sum = sum(array)  # calculate sum of array elements
        missing_element = total_sum - array_sum  # calculate missing element
        return missing_element
