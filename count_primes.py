# https://leetcode.com/problems/count-primes/description/
# 204. Count Primes
# Explanation: https://algo.monster/liteproblems/204
# the Sieve of Eratosthenes algorithm

# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0

# Constraints:
# 0 <= n <= 5 * 106

class Solution:
    def countPrimes(self, n: int) -> int:
        ''' Count Primes '''
        primes = [True] * n
        out = 0
        for i in range(2, n):
            if primes[i]:
                out += 1
                for j in range(i + i, n, i):
                    primes[j] = False
        return out

print(Solution().countPrimes(10))
# Output: 4
print(Solution().countPrimes(0))
# Output: 0
print(Solution().countPrimes(1))
# Output: 0
