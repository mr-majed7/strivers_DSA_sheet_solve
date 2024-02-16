#https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
#https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_5713505?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a)
    prevSum = {}
    sum = 0
    maxLen = 0

    for i in range(n):
        sum +=a[i]

        if sum == k:
            maxLen = max(maxLen,i+1)

        rem = sum-k

        if rem in prevSum:
            length = i - prevSum[rem]
            maxLen = max(maxLen,length)
        
        if sum not in prevSum:
            prevSum[sum] = i
    return maxLen
