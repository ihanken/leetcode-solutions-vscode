#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyOne = buyTwo = float('inf')
        sellOne = sellTwo = 0

        for price in prices:
            sellTwo = max(sellTwo, price - buyTwo)
            buyTwo = min(buyTwo, price - sellOne)

            sellOne = max(sellOne, price - buyOne)
            buyOne = min(buyOne, price)

        return sellTwo

