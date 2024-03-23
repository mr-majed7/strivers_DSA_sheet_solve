# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    """
    This is a simple problem of finding the maximum difference between two elements in the array.
    The difference should be such that the larger element appears after the smaller element.
    We can solve this problem by keeping track of the minimum element found so far and the maximum difference found so far.
    We iterate through the array and update the minimum element and the maximum difference as we go along.
    """

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0  # initialize the profit to 0
        min_p = prices[
            0
        ]  # initialize the minimum price to the first element in the array
        for i in range(1, len(prices)):
            cost = (
                prices[i] - min_p
            )  # calculate the difference between the current price and the minimum price
            profit = max(
                profit, cost
            )  # update the profit to the maximum of the current profit and the difference
            min_p = min(
                min_p, prices[i]
            )  # update the minimum price to the minimum of the current minimum price and the current price
        return profit
