# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/


class Solution:
    """
    Initilizare an array of the same length as the input array
    Initialize two pointers, one for positive numbers and one for negative numbers
    For each positive or negative number, add it to the answer array and increment the pointer by 2 to skip the next position
    """

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        answer = [0] * len(
            nums
        )  # initilize an array of the same length as the input array
        pos_i = 0  # pointer for positive numbers
        neg_i = 1  # pointer for negative numbers
        for n in nums:
            if n >= 0:  # if the number is positive
                answer[pos_i] = n  # add it to the answer array
                pos_i += 2  # increment the pointer by 2 to skip the next position
            else:  # if the number is negative
                answer[neg_i] = n  # add it to the answer array
                neg_i += 2  # increment the pointer by 2 to skip the next position
        return answer
