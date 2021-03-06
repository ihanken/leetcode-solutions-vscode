#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (25.36%)
# Total Accepted:    125.6K
# Total Submissions: 491.5K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def cmp(a, b):
            return int(b + a) - int(a + b)
        
        nums = sorted(list(map(str, nums)), key = cmp_to_key(cmp))

        return ''.join(nums).lstrip('0') or '0'
        

