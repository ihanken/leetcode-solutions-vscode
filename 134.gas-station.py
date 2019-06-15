#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        current = 0
        start = 0

        for i in range(0, len(gas)):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if current < 0:
                current = 0
                start = i + 1

        return -1 if total < 0 else start


