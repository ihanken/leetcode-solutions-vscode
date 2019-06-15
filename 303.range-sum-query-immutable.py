#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
class NumArray:

    def __init__(self, nums: List[int]):
        self.cachedNums = nums[:]

        for i in range(1, len(self.cachedNums)):
            self.cachedNums[i] += self.cachedNums[i - 1]
        

    def sumRange(self, i: int, j: int) -> int:
        if i == 0: return self.cachedNums[j]

        return self.cachedNums[j] - self.cachedNums[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

