# https://leetcode.com/problems/maximum-subarray/description/


class Solution:
    """
    Here we are using Kadane's algorithm to solve the problem. The algorithm is as follows:
    1. Initialize:
        max_so_far = 0
        max_ending_here = 0
    2. Loop for each element of the array
         (a) max_ending_here = max_ending_here + a[i]
         (b) if(max_ending_here < 0)
         max_ending_here = 0
         (c) if(max_so_far < max_ending_here)
         max_so_far = max_ending_here
    3. return max_so_far
    """

    def maxSubArray(self, nums: List[int]) -> int:
        subarry = nums[0]  # initialize the subarray to the first element (max_so_far)
        maximum = 0  # initialize the maximum to 0 (max_ending_here)
        for i in nums:
            maximum += i  # add the current element to the maximum
            subarry = max(
                subarry, maximum
            )  # update the subarray to the maximum of the subarray and maximum
            if maximum < 0:  # if maximum is less than 0, then reset maximum to 0
                maximum = 0
        return subarry  # return the subarray
