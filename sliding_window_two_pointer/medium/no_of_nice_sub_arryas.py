# https://leetcode.com/problems/count-number-of-nice-subarrays/


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            count = 0
            left = 0

            total = 0

            for right in range(len(nums)):
                total += nums[right] % 2
                while total > x:
                    total -= nums[left] % 2
                    left += 1

                count += right - left + 1
            return count

        return helper(k) - helper(k - 1)
