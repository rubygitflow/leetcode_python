# https://leetcode.com/problems/network-delay-time/description/
# 743. Network Delay Time

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

# Example 2:
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1

# Example 3:
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

# Constraints:
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ''' Network Delay Time '''
        # полный массив выходных узлов
        outs = set()
        # полный массив входных узлов
        nodes = defaultdict(list)
        for u, v, w in times:
            outs.add(v)
            nodes[u].append([v, w])
        # print('nodes',nodes)
        # {2: [[1, 1], [3, 1]], 3: [[4, 1]]}
        # реальный массив начальных узлов (может быть не весь охвачен сигналом)
        if k not in set(nodes).difference(outs):
            return -1
        # реальный массив конечных узлов, до которых будем считать временные расстояния:
        # это будет МАКСИМУМ для разных конечных узлов и
        # МИНИМУМ для одинаковых конечных узлов от разных путей доставки сигнала
        outs = outs.difference(nodes.keys())
        minmax_outs = {}
        for i in outs:
            minmax_outs[i] = 2 ** 31
        # (Depth First Searching)
        def dfs(i: int, dist: int):
            for el in nodes[i]:
                dfs(el[0], dist + el[1])
            if i in outs:
                minmax_outs[i] = min(minmax_outs[i], dist)
        dfs(k, 0)
        return max(minmax_outs.values())

times, n, k = [[2,1,1],[2,3,1],[3,4,1]], 4, 2
Output: 2
times, n, k = [[1,2,1]], 2, 1
Output: 1
times, n, k = [[1,2,1]], 2, 2
Output: -1
Solution().networkDelayTime(times, n, k)
