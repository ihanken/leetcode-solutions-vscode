#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        
        if len(preorder) < 1: return False
        
        diff = 1
        
        for char in preorder:
            diff -= 1
            if diff < 0: return False
            if char != '#': diff += 2
                
        return diff == 0

