# https://leetcode.com/problems/move-zeroes/description/


class Solution:
    """
    Here we taake a pointer j to find the first occurance of 0.
    Then we iterate through teh array from the first 0 to the end of the array.
    If we find a non zero element we swap it with the first 0 element and increment the pointer j.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
