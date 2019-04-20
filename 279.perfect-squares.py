#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (41.12%)
# Total Accepted:    174.2K
# Total Submissions: 419.8K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
class Solution:
    _dp = [0]

    def numSquares(self, n):
        dp = self._dp

        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,

        return dp[n]

