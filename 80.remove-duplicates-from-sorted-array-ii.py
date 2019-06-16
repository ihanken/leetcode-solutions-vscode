#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2

        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1] == nums[i - 2]:
                del nums[i]

            i += 1

        return len(nums)

