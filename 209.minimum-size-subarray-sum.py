#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = j = 0
        currentSum = 0
        minLength = float('inf')

        while i <= j < len(nums):
            currentSum += nums[j]

            while i <= j and currentSum >= s:
                minLength = min(minLength, j - i + 1)

                currentSum -= nums[i]
                i += 1

            j += 1

        return minLength if minLength < float('inf') else 0

