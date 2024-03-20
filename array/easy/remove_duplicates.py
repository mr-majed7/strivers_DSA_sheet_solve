# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    """
    Here two pointers approach is taken.
    This first point i used to keep track of the unique elements.
    The second pointer j is used to iterate through the array.
    If the element at i and j are same, then we don't do anything.
    If the element at i and j are different, then we increment i and replace the element at i with the element at j.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
