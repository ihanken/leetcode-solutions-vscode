#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        maxFound = 0
        minBuy = prices[0]

        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i])
            maxFound = max(maxFound, prices[i] - minBuy)

        return maxFound
        

