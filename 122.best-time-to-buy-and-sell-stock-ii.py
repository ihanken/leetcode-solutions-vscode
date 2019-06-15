#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        totalProfit = 0
        currentMinPrice = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > currentMinPrice:
                totalProfit += prices[i] - currentMinPrice
                currentMinPrice = prices[i]
            else:
               currentMinPrice = prices[i]

        return totalProfit

