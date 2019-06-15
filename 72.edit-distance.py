#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        record = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            record[i][0] = i

        for j in range(n + 1):
            record[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    record[i][j] = record[i - 1][j - 1]
                else:
                    record[i][j] = 1 + min(record[i - 1][j], record[i][j - 1], record[i - 1][j - 1])

        return record[-1][-1]

