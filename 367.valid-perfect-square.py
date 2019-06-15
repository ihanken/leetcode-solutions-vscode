#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num

        while (low <= high):
            mid = low + (high - low) // 2
            squared = mid ** 2

            if squared == num: return True
            elif squared > num: high = mid - 1
            else: low = mid + 1

        return False

