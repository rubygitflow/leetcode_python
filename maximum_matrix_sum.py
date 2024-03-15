# https://leetcode.com/problems/maximum-matrix-sum/description/
# 1975. Maximum Matrix Sum

# You are given an n x n integer matrix. You can do the following operation any number of times:
# Choose any two adjacent elements of matrix and multiply each of them by -1.
# Two elements are considered adjacent if and only if they share a border.
# Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

# Example 1:
# Input: matrix = [[1,-1],[-1,1]]
# Output: 4
# Explanation: We can follow the following steps to reach sum equals 4:
# - Multiply the 2 elements in the first row by -1.
# - Multiply the 2 elements in the first column by -1.
# Example 2:
# Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
# Output: 16
# Explanation: We can follow the following step to reach sum equals 16:
# - Multiply the 2 last elements in the second row by -1.

# Constraints:
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105

from typing import List
from numpy import inf

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    '''
    для ЧЕТНОГО количества отрицательных чисел можем обойтись перемножением на [-1,-1] любое количество раз
    для нечетного количества отрицательных чисел надо найти минимальное число в матрице, чтобы его заминусовать
    '''
        total = cnt = 0
        mi = inf
        for row in matrix:
            for v in row:
                total += abs(v)
                mi = min(mi, abs(v))
                if v < 0:
                    cnt += 1
        if cnt % 2 == 0 or mi == 0:
            return total
        return total - mi * 2


matrix = [[1,-1],[-1,1]]
Output: 4
matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Solution().maxMatrixSum(matrix)
