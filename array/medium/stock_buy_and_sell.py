#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = prices[0]
        for i in range(1,len(prices)):
            cost = prices[i] - min_p
            profit = max(profit,cost)
            min_p = min(min_p,prices[i])
        return profit
