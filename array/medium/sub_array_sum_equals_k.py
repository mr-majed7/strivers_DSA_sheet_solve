# https://leetcode.com/problems/subarray-sum-equals-k/description/


class Solution:
    """
    We can use a hashmap to store the sum of the subarray from index 0 to i.
    We use the concept of prefix sum.
    We add the prefix sum to the hashmap.
    To find the subarray sum, we subtract the prefix sum from the current sum.
    We increment the count by the value of the prefix sum in the hashmap.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum_map = defaultdict(int)
        count = 0
        pre_sum = 0

        pre_sum_map[0] = 1

        for i in nums:
            pre_sum += i

            remove = pre_sum - k

            count += pre_sum_map[remove]

            pre_sum_map[pre_sum] += 1

        return count
