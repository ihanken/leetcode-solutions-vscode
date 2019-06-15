#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
class Solution:
    def normalizeString(self, s: str) -> str:
        """
        This lowercases the string and removes all characters other than alphanumeric ones.
        """
        return ''.join([c.lower() for c in s if c.isalnum()])

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True

        alteredS = self.normalizeString(s)

        return alteredS == alteredS[::-1]
        

