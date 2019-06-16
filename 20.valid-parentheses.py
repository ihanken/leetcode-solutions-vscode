#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
PAREN_DICT = {
    ')': '(',
    ']': '[',
    '}': '{'
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in PAREN_DICT:
                if not stack or stack[-1] != PAREN_DICT[char]: return False
                
                stack.pop()
            else:
                stack.append(char)

        return not stack

        

