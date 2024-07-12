# https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
class Solution:
    # Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self, n):
        # code here
        count = 0
        for i in range(1, n + 1):
            while i != 0:
                i = i & i - 1
                count += 1
        return count
