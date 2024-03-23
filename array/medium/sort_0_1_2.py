# https://leetcode.com/problems/sort-colors/description/


class Solution:
    """
    To solve this problem we will use the Dutch National Flag algorithm.
    The algorithm maintains three pointers low, mid and high. The idea is to keep 0s before low, 1s before mid and 2s after high.

    """

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:  # Swap low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1  # Increment low
                mid += 1  # Increment mid
            elif nums[mid] == 1:  # Increment mid if we get 1
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]  # Swap mid and high
                high -= 1  # Decrement high
