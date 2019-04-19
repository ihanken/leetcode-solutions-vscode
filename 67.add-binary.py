#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.21%)
# Total Accepted:    291.8K
# Total Submissions: 755.5K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if '' in (a, b): return a or b
        
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary('1', self.addBinary(a[:-1], b[:-1])) + '0'
        
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        
        return self.addBinary(a[:-1], b[:-1]) + '1'
            
        

