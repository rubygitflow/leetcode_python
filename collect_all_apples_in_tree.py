# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
# 1443. Minimum Time to Collect All Apples in a Tree

# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.
# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

# Example 1:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

# Example 2:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  

# Example 3:
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
# Output: 0

# Constraints:
# 1 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# hasApple.length == n

from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(u, cost):
            # skip visited paths
            if vis[u]:
                return 0
            vis[u] = True
            nxt_cost = 0
            # collect all paths
            for v in g[u]:
                nxt_cost += dfs(v, 2)
            # print('u',u,'cost',cost,'nxt_cost',nxt_cost, 'hasApple[u]',hasApple[u])
            if not hasApple[u] and nxt_cost == 0:
                return 0
            # print('u',u,'cost',cost,'nxt_cost',nxt_cost)
            # add "last mile" cost
            return cost + nxt_cost

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [False] * n
        # print(g)
        return dfs(0, 0)


print(Solution().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]))
# Output: 8 
print(Solution().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,False,True,False]))
# Output: 6
print(Solution().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,False,False,False,False,False]))
# Output: 0
print(Solution().minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[True,False,False,False,False,False,False]))
# Output: 0
print(Solution().minTime(9,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]],[False,False,False,False,False,False,False,False,True]))
# Output: 6
print(Solution().minTime(9,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]],[False,True,False,False,True,False,False,False,True]))
# Output: 6
