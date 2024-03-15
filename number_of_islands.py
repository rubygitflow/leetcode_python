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

##########################
# https://leetcode.com/problems/number-of-islands-ii/description/
# 305. Number of Islands II

# You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).
# We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.
# Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]
# Explanation:
# Initially, the 2d grid is filled with water.
# - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
# - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
# - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
# - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.

# Example 2:
# Input: m = 1, n = 1, positions = [[0,0]]
# Output: [1]

# Constraints:
# 1 <= m, n, positions.length <= 104
# 1 <= m * n <= 104
# positions[i].length == 2
# 0 <= ri < m
# 0 <= ci < n

# Follow up: Could you solve it in time complexity O(k log(mn)), where k == positions.length?

from typing import List
import time

def numIslands(grid: List[List[str]]) -> int:
    ''' Number of Islands Alg.V1 '''
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
    ''' Number of Islands Alg.V2 '''
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

#########
def numOfIslandsII(m: int, n: int, positions: List[List[int]]) -> List[int]:
    ''' Number of Islands II '''
    def check(i, j):
        return 0 <= i < m and 0 <= j < n and grid[i][j] == 1
    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    p = list(range(m * n))
    grid = [[0] * n for _ in range(m)]
    res = []
    cur = 0 # current island count
    for i, j in positions:
        if grid[i][j] == 1: # already counted, same as previous island count
            res.append(cur)
            continue
        grid[i][j] = 1
        cur += 1
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if check(i + x, j + y) and find(i * n + j) != find((i + x) * n + j + y):
                p[find(i * n + j)] = find((i + x) * n + j + y)
                cur -= 1
                # 1 0 1
                # 0 1 0
                # for above, if setting 1st-row 2nd-col 0-to-1
                # cur will -1 for 3 times
                # but cur += 1 after grid[i][j] = 1 so cur final result is 1
        res.append(cur)
    return res

m, n, positions = 3, 3, [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]
m, n, positions = 1, 1, [[0,0]]
# Output: [1]
numOfIslandsII(m, n, positions)
