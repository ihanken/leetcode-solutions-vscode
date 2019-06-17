#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
class Solution:
    def normalizeString(self, s: str) -> str:
        record = dict()
        normalChar = 'a'

        for char in s:
            if char not in record:
                record[char] = normalChar
                normalChar = chr(ord(normalChar) + 1)

        newString = ""

        for char in s:
            newString += record[char]

        return newString

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.normalizeString(s) == self.normalizeString(t)

