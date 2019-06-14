#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                del nums[i]

            i += 1

        return len(nums)

