# https://leetcode.com/problems/sum-of-subarray-ranges/


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
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

        def sumSubArrayMin(nums):
            total = 0
            pse = getPse(nums)
            nse = getNse(nums)
            for i in range(len(nums)):
                left = i - pse[i]
                right = nse[i] - i
                total += (right * left) * nums[i]
            return total

        def getNge(nums):
            nge = [len(nums)] * len(nums)
            st = []

            for i in range(len(nums)):
                while st and nums[st[-1]] < nums[i]:
                    nge[st.pop()] = i
                st.append(i)
            return nge

        def getPge(nums):
            pge = [-1] * len(nums)
            st = []

            for i in range(len(nums) - 1, -1, -1):
                while st and nums[st[-1]] <= nums[i]:
                    pge[st.pop()] = i
                st.append(i)
            return pge

        def sumSubArrayMax(nums):
            total = 0
            nge = getNge(nums)
            pge = getPge(nums)

            for i in range(len(nums)):
                left = i - pge[i]
                right = nge[i] - i
                total += (right * left) * nums[i]

            return total

        largest_sum = sumSubArrayMax(nums)
        smallest_sum = sumSubArrayMin(nums)
        return largest_sum - smallest_sum
