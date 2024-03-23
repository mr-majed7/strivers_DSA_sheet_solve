##https://leetcode.com/problems/two-sum/description/


class Solution:
    """
    An approach to solve the problem is to use a hash table to store the numbers and their indices.
    We iterate through the list of numbers and for each number, we check if the difference between the target and the number is in the hash table.
    If it is, we return the indices of the two numbers.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
