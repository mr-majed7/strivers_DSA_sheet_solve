# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0
        zeroes = 0

        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes +=1
            
            if zeroes >k:
                if nums[left] == 0:
                    zeroes -=1
                left +=1

            if zeroes <= k:
                max_length = max(max_length,right-left+1)
            right +=1
        
        return max_length
