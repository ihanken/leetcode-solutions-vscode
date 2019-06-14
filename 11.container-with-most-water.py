#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxWater = 0

        while left < right:
            maxHeight = min(height[left], height[right])
            maxWater = max(maxWater, maxHeight * (right - left))

            while height[left] <= maxHeight and left < right: left += 1
            while height[right] <= maxHeight and left < right: right -= 1

        return maxWater
        

