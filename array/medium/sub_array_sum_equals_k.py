#https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            pre_sum_map = defaultdict(int)
            count = 0
            pre_sum = 0

            pre_sum_map[0] = 1

            for i in nums:
                pre_sum += i

                remove = pre_sum - k

                count +=pre_sum_map[remove]
                
                pre_sum_map[pre_sum] += 1

            return count
