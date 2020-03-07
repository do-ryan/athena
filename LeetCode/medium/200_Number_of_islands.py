"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_counter = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == '1':
                    island_counter += 1
                    bfs_queue = [(i, j)]
                    while bfs_queue:
                        un = bfs_queue.pop(0)
                        for neighbour in [(un[0]-1, un[1]), (un[0], un[1]-1), (un[0]+1, un[1]), (un[0], un[1]+1)]:
                            if neighbour[0] < 0 or neighbour[0] >= len(grid) or neighbour[1] < 0 or neighbour[1] >= len(grid[0]):
                                continue
                            else:
                                if grid[neighbour[0]][neighbour[1]] == '1':
                                    grid[neighbour[0]][neighbour[1]] = '0'
                                    bfs_queue.append(neighbour)
        return island_counter




