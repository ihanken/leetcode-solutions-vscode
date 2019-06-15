#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        localMax = globalMax = nums[0]

        for i in range(1, len(nums)):
            localMax = max(nums[i], localMax + nums[i])
            globalMax = max(globalMax, localMax)

        return globalMax

