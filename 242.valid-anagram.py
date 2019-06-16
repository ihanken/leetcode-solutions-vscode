#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        if len(s) == 0 and len(t) == 0: return True
        
        charArr = [0] * 26

        for i in range(len(s)):
            charArr[ord(s[i]) - ord('a')] += 1
            charArr[ord(t[i]) - ord('a')] -= 1

        for charCount in charArr:
            if charCount > 0: return False

        return True

