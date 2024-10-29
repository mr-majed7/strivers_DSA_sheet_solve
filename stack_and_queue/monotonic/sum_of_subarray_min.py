# https://leetcode.com/problems/sum-of-subarray-minimums/


from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def getNse(nums):
            nse = [len(nums)] * len(nums)
            st = []

            for i in range(len(nums)):
                while st and nums[st[-1]] > nums[i]:
                    nse[st.pop()] = i
                st.append(i)
            return nse

        def getPse(nums):
            pse = [-1] * len(nums)
            st = []

            for i in range(len(nums) - 1, -1, -1):
                while st and nums[st[-1]] >= nums[i]:
                    pse[st.pop()] = i
                st.append(i)
            return pse

        total = 0
        Mod = 10**9 + 7

        nse = getNse(arr)
        pse = getPse(arr)

        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + (right * left * arr[i]) % Mod) % Mod

        return total
