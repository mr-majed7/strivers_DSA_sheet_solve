# https://leetcode.com/problems/majority-element/description/


class Solution:
    """
    We can solve this problem using Boyer-Moore Voting Algorithm.
    The idea is to cancel out each occurrence of an element e with all the other elements that are different from e.
    This way e will exist till end if it is a majority element.
    """

    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        el = 0
        for i in nums:
            if count == 0:  # if count is 0, then we have a new element
                el = i  # set the new element
                count = 1  # set the count to 1
            elif i == el:  # if the element is same as the current element
                count += 1  # increment the count
            else:  # if the element is different from the current element
                count -= 1  # decrement the count
        return el
