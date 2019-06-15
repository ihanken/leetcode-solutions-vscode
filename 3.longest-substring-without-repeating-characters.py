#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        maxLength = 0
        record = set()

        while i <= j < len(s):
            while s[j] in record:
                record.remove(s[i])
                i += 1

            record.add(s[j])
            j += 1

            maxLength = max(maxLength, j - i)

        return maxLength


