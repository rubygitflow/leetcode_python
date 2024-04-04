# https://leetcode.com/problems/critical-connections-in-a-network/description/
# 1192. Critical Connections in a Network

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
# Return all critical connections in the network in any order.

# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

# Example 2:
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]

# Constraints:
# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.

from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ''' Critical Connections in a Network '''
        bridges = []
        visited = set()
        graph = defaultdict(list)
        # graph = [[] for _ in range(n)]
        self.times = 0
        discovered = [0] * n
        lowest = [0] * n
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(cur,prev):
            visited.add(cur)
            self.times += 1
            discovered[cur] = lowest[cur] = self.times
            # print(cur,'1. lowest = ',lowest, '; discovered = ',discovered)
            for node in graph[cur]:
                if node not in visited:
                    # print(cur,'2.1. self.times',self.times)
                    dfs(node, cur)
                    lowest[cur] = min(lowest[cur], lowest[node])
                    # print(cur,'4.1. lowest',lowest)
                elif node != prev:
                    lowest[cur] = min(lowest[cur], discovered[node])
                    # print(cur,'2.2. lowest',lowest)
                # print('2.3. cur, node , lowest[node], discovered[cur]',cur, node , lowest[node], discovered[cur])
                if lowest[node] > discovered[cur]:
                    bridges.append([cur, node])
                    # print(cur,'3.1. bridges',bridges)
                # else:
                #     print(cur,'3.2. <<<')
        for i in range(0,n):
            if i not in visited:
                dfs(i,-1)
                # print('lowest = ',lowest, '; discovered = ',discovered)
        return bridges


print(Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))
# Output: [[1,3]]
print(Solution().criticalConnections(2, [[0,1]]))
# Output: [[0,1]]
# infinity sign
print(Solution().criticalConnections(5, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,1]]))
# Output: []
# dumbbell
print(Solution().criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))
# Output: [[1,3]]
# 2 donuts
print(Solution().criticalConnections(7, [[0,1],[1,2],[2,0],      [3,4],[4,5],[5,3],[5,6]]))
# Output: [[5,6]]
# star
print(Solution().criticalConnections(7, [[0,1],[0,2],[2,3],[0,4],[0,5],[5,6]]))
# Output: [[0, 1], [2, 3], [0, 2], [0, 4], [5, 6], [0, 5]]
