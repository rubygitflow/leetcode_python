# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# 1735. Count Ways to Make Array With Product

# You are given a 2D integer array, queries. For each queries[i], where queries[i] = [ni, ki], find the number of different ways you can place positive integers into an array of size ni such that the product of the integers is ki. As the number of ways may be too large, the answer to the ith query is the number of ways modulo 109 + 7.
# Return an integer array answer where answer.length == queries.length, and answer[i] is the answer to the ith query.

# Example 1:
# Input: queries = [[2,6],[5,1],[73,660]]
# Output: [4,1,50734910]
# Explanation: Each query is independent.
# [2,6]: There are 4 ways to fill an array of size 2 that multiply to 6: [1,6], [2,3], [3,2], [6,1].
# [5,1]: There is 1 way to fill an array of size 5 that multiply to 1: [1,1,1,1,1].
# [73,660]: There are 1050734917 ways to fill an array of size 73 that multiply to 660. 1050734917 modulo 109 + 7 = 50734910.

# Example 2:
# Input: queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: [1,2,3,10,5]

# Constraints:
# 1 <= queries.length <= 104 
# 1 <= ni, ki <= 104

from typing import List
from collections import defaultdict

N = 10020
MOD = 10**9 + 7
f = [1] * N
g = [1] * N
p = defaultdict(list)
for i in range(1, N):
    f[i] = f[i - 1] * i % MOD
    g[i] = pow(f[i], MOD - 2, MOD)
    x = i
    j = 2
    while j <= x // j:
        if x % j == 0:
            cnt = 0
            while x % j == 0:
                cnt += 1
                x //= j
            p[i].append(cnt)
        j += 1
    if x > 1:
        p[i].append(1)

def comb(n, k):
    return f[n] * g[k] * g[n - k] % MOD

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ''' Count Ways to Make Array With Product '''
        output = []
        for n, k in queries:
            t = 1
            for x in p[k]:
                t = t * comb(x + n - 1, n - 1) % MOD
            output.append(t)
        return output

queries = [[2,6],[5,1],[73,660]]
# Output: [4,1,50734910]       
queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# Output: [1,2,3,10,5]
Solution().waysToFillArray(queries)
