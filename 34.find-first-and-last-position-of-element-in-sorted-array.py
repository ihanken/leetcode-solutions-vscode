#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        if not nums: return result

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] < target: low = mid + 1
            else: high = mid

        if nums[low] != target: return result
        else: result[0] = low
        
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2 + 1

            if nums[mid] > target: high = mid - 1
            else: low = mid
        
        result[1] = high

        return result
