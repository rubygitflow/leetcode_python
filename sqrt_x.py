# https://leetcode.com/problems/sqrtx/description/
# 69. Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        ''' Sqrt(x) - binary search '''
        l, r = 0, x
        while l < r:
          middle = (l + r + 1) >> 1
          square = middle * middle
          if square == x: return middle

          if square < x:
              l = middle
          else:
              r = middle - 1

        return l

print(Solution().mySqrt(4))
# Output: 2
print(Solution().mySqrt(8))
# Output: 2
print(Solution().mySqrt(1))
# Output: 1
print(Solution().mySqrt(0))
# Output: 0
print(Solution().mySqrt(2**31 - 1))
# Output: 46340
print(Solution().mySqrt(2147395601))
# Output: 46340
