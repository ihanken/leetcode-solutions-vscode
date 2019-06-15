#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        record = [MAX] * (amount + 1)
        record[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    record[i] = min(record[i - coin] + 1, record[i])

        return -1 if record[-1] == MAX else record[-1]
