# https://leetcode.com/problems/search-in-rotated-sorted-numsay/


class Solution:
    """
    After rotation either the left half or the right half of
    the array will be sorted.
    First, find out which portion or the array is sorted.
    Check if that portion have the target value.
    If it does eliminate other half.
    Otherwise eliminate the sorted half
    """

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:  # Check If Left Half is Sorted
                if (
                    nums[low] <= target and nums[mid] > target
                ):  # Check if the Target is in the Left Half
                    high = mid - 1  # Eliminate the Right Half
                else:
                    low = (
                        mid + 1
                    )  # If target is not in the left half eliminate left half
            else:
                if (
                    nums[mid] <= target and nums[high] >= target
                ):  # The Right Half is sorted
                    low = (
                        mid + 1
                    )  # Eliminate Left Half as the Target is in the Right Half
                else:
                    high = (
                        mid - 1
                    )  # Eliminate Right Half as the Target is in the Left Half
        return -1


"""
Here Which half is sorted is being checked to
know in which portion the target value is in.
For instance, if in a array the left portion is sorted and 
the target value is in the left half then target will be greater than
the lower value of left half and lesser than mid value.
"""
