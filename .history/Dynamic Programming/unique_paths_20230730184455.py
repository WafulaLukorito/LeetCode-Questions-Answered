
"""
Unique Paths (Leetcode 62)
Medium: DP
Link: https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?




"""
class Solution:
    def unique_paths(self, grid):
        
        row_length= len(grid)
        col_length= len(grid[0])
        
        dp= [[0 for _in range(col_length)] for _in range (row_length)]
    
        for i in range (row_length):
            for j in range (col_length):
                if (i == 0) or (j==0):
                    dp[i][j]=1
        
        for i in range (1, row_length):
            for j in range(1, col_length):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return (dp[row_length-1][col_length-1])
    