#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def fillIsland(self, grid: List[List[str]], i: int, j: int):
        if grid[i][j] != '1': return

        grid[i][j] = '0'

        # Move down
        if i < len(grid) - 1: self.fillIsland(grid, i + 1, j)
        
        # Move up
        if i > 0: self.fillIsland(grid, i - 1, j)
        
        # Move right
        if j < len(grid[i]) - 1: self.fillIsland(grid, i, j + 1)
        
        # Move left
        if j > 0: self.fillIsland(grid, i, j - 1)
        

    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    islandCount += 1
                    self.fillIsland(grid, i, j)

        return islandCount
