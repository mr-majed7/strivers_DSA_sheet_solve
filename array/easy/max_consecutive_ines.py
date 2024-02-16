#https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        count = 0
        for i in (nums):
            if i == 1:
                count +=1
            else:
                if count >=max:
                    max = count
                count = 0
        if count >=max:
            max = count
        return max