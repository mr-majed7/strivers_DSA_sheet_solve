# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                first = mid
                high = mid - 1
            else:
                low = mid + 1
        low = 0
        high = len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if first == -1 or last == -1:
            return [-1, -1]
        else:
            return [first, last]
