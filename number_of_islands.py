# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List
import time

def numIslands(grid: List[List[str]]) -> int:
    t = time.time()
    n=len(grid)
    m=len(grid[0])
    visited=[[-1 for j in range(m)]for i in range(n)]
    # available values:
    # 0 - see
    # int>0 - through island number = island
    island = 0
    linked_list = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='1':
                # 2
                # ?
                if i > 0 and visited[i-1][j] > 0:
                    visited[i][j] = visited[i-1][j]
                    # 102
                    # 11?
                    if visited[i][j] != island:
                        linked_list[island] = visited[i][j]
                # 00
                # 1?
                elif j > 0 and visited[i][j-1] > 0:
                    visited[i][j] = visited[i][j-1]
                else:
                    # 0?
                    island += 1
                    visited[i][j] = island
            else:
                visited[i][j] = 0
    print(time.time()-t)
    return island - len(linked_list)

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# 4.601478576660156e-05
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3
# 2.5987625122070312e-05
numIslands(grid)


def numIslandsII(grid: List[List[str]]) -> int:
    t = time.time()
    m = len(grid)
    n = len(grid[0])
    # затираем остров целиком,
    # чтобы не пересекаться с ним из основного алгоритма
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                ans += 1
                dfs(i, j)
    print(time.time()-t)
    return ans

numIslandsII(grid)

# 2.6702880859375e-05
