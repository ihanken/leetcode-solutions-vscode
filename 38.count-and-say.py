#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for i in range(2, n + 1):
            j = 0
            newString = ""

            while j < len(current):
                currentChar = current[j]
                count = 1
                j += 1

                while j < len(current) and current[j] == currentChar:
                    j += 1
                    count += 1

                newString += str(count) + currentChar

            current = newString

        return current

