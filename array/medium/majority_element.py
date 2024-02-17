#https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        el = 0
        for i in nums:
            if count == 0:
                el = i
                count = 1
            elif i == el:
                count +=1
            else:
                count -=1
        return el