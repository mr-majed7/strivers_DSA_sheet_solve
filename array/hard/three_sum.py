#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for l in range(n):
            if (l!=0 and nums[l]==nums[l-1]):
                continue

            m = l+1
            r =  n-1

            while m < r:
                sum = nums[l] + nums[m] + nums[r]
                if sum < 0:
                    m +=1
                elif sum > 0:
                    r -=1
                else:
                    res.append([nums[l],nums[m],nums[r]])
                    m +=1
                    while m < r and nums[m] == nums[m-1]:
                        m +=1
        return res
