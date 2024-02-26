#https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el_1,el_2 = float('inf'),float('inf')
        count_1,count_2 = 0,0

        for i in nums:
            if count_1 == 0 and el_2 !=i:
                el_1 = i
                count_1 = 1
            elif count_2 == 0 and el_1 !=i:
                el_2 = i
                count_2 = 1
            elif i == el_1:
                count_1 +=1
            elif i == el_2:
                count_2 +=1
            else:
                count_1 -=1
                count_2 -=1

        res = []
        count_1,count_2 = 0,0
        for i in nums:
            if i == el_1:
                count_1 +=1
            elif i == el_2:
                count_2 +=1
        if count_1 > len(nums)/3:
            res.append(el_1)
        if count_2 > len(nums)/3:
            res.append(el_2)
        
        return res
        
        
