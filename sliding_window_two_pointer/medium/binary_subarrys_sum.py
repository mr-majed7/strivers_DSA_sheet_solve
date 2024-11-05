# https://leetcode.com/problems/binary-subarrays-with-sum/


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            count = 0
            left = 0

            total = 0

            for right in range(len(nums)):
                total += nums[right]
                while total > x:
                    total -= nums[left]
                    left += 1

                count += right - left + 1
            return count

        return helper(goal) - helper(goal - 1)
