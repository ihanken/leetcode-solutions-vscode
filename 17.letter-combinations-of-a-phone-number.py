#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

NUMS_TO_LETTERS = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    def solve(self, digits: str, currentStr: str, result):
        if len(digits) < 1 and len(currentStr) > 0:
            result.append(currentStr)
            return

        for char in NUMS_TO_LETTERS[digits[0]]:
            self.solve(digits[1:], currentStr + char, result)

        return result

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        result = []

        self.solve(digits, "", result)

        return result

