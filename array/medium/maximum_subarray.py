#https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarry = nums[0]
        maximum = 0
        for i in nums:
            maximum +=i
            subarry = max(subarry,maximum)
            if maximum<0:
                maximum = 0
        return subarry