#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Since a number XORed with itself is 0, we can just XOR all the numbers in the array.
        The only number left will be the number that isn't repeated.
        """
        record = 0

        for num in nums:
            record ^= num
        
        return record
        

