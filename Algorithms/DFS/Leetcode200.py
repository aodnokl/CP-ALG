# ==========================================
# PROBLEM: 200. Number of Islands (Medium)
# ==========================================
# Description:
# Given an m x n 2D binary grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent 
# lands horizontally or vertically. You may assume all four edges of the 
# grid are all surrounded by water.
#
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# - m == grid.length
# - n == grid[i].length
# - 1 <= m, n <= 300
# - grid[i][j] is '0' or '1'


from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Base case
        if not grid:
            return 0

        # Init of variables
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        
        def dfs(row, col):
            # Check bounds
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0':
                return

            # Mark the current cell as visited by turning it to 0
            grid[row][col] = '0'

            # Make all adj dirrections
            dirrections  = [
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1)
            ]

            # Explore all dirrection with recusion
            for n_row, n_col in dirrections:
                dfs(n_row, n_col)


        for r in range(rows):
            for c in range(cols):
                # If we find a land ('1') it's new island
                if grid[r][c] == '1':
                    island_count += 1
                    # To visit the entire connected island
                    dfs(r, c)

        return island_count