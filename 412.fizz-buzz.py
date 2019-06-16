#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            returnStr = ""

            if i % 3 == 0: returnStr += "Fizz"
            if i % 5 == 0: returnStr += "Buzz"
            
            if returnStr == "": returnStr = str(i)

            result.append(returnStr)

        return result

