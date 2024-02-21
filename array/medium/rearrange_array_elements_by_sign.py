#https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        pos_i = 0
        neg_i = 1
        for n in nums:
            if n >=0:
                answer[pos_i] = n
                pos_i +=2
            else:
                answer[neg_i] = n
                neg_i +=2
        return answer
