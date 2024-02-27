#https://www.codingninjas.com/studio/problems/longest-subarray-with-zero-sum_6783450?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    # Write your code here.
    preSum = {}
    sum = 0
    maxi = 0
    for i in range(len(arr)):
        sum +=arr[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in preSum:
                maxi = max(maxi,i-preSum[sum])
            else:
                preSum[sum] = i
    return maxi
