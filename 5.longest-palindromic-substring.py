#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.79%)
# Total Accepted:    523.9K
# Total Submissions: 1.9M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def expandFromCenter(self, text: str, i: int, j: int):
        '''
        This function returns the longest palindromic substring in a string when expanding from a start and end index.
        The function expects the start and end index to either be equal or differ by one.

        Parameters:
        text (str): the text to search for palindromes in
        i (int): the start index
        j (int): the end index

        Returns:
        str: the longest palindromic substring found
        '''

        if text[i] != text[j]: return ""

        while i - 1 >= 0 and j + 1 < len(text) and text[i - 1] == text[j + 1]:
            i -= 1
            j += 1

        return text[i:j + 1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        
        maxWord = s[0]

        for i in range(1, len(s)):
            sameIndex = self.expandFromCenter(s, i, i)
            differentIndex = self.expandFromCenter(s, i - 1, i)

            if len(sameIndex) > len(maxWord): maxWord = sameIndex
            if len(differentIndex) > len(maxWord): maxWord = differentIndex

        return maxWord
