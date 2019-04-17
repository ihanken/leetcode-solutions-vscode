#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element/description/
#
# algorithms
# Easy (43.81%)
# Total Accepted:    381.7K
# Total Submissions: 871.3K
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array nums and a value val, remove all instances of that value
# in-place and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# Example 1:
# 
# 
# Given nums = [3,2,2,3], val = 3,
# 
# Your function should return length = 2, with the first two elements of nums
# being 2.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# 
# Example 2:
# 
# 
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# 
# Your function should return length = 5, with the first five elements of nums
# containing 0, 1, 3, 0, and 4.
# 
# Note that the order of those five elements can be arbitrary.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0                       # The pointer for the element we want to look at
        backPointer = len(nums) - 1 # The pointer used to keep track of where we are moving elements we want to remove

        while i <= backPointer:                                         # Only iterate until we reach backPointer
            while i <= backPointer and nums[i] == val:                  # While we are sitting on an element we should remove
                nums[i], nums[backPointer] = nums[backPointer], nums[i] # Swap the element and the element sitting at backPointer
                backPointer -= 1                                        # Decrement backPointer
            
            i += 1                                                      # Once we have an element that shouldn't be removed, increment i.


        nums = nums[:backPointer + 1] if backPointer >= 0 else []       # Return an empty list if the list was only made up of invalid
                                                                        # elements, otherwise slice it based on backPointer
        return len(nums)

