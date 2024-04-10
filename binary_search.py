# https://leetcode.com/problems/binary-search/description/
# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

########################
# https://leetcode.com/problems/search-a-2d-matrix/description/
# 74. Search a 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' Binary Search '''
        l, r = 0, len(nums) - 1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #left direction
            elif nums[mid] > target:
                r = mid - 1
            #right direction
            else:
                l = mid + 1
        #ends when r < l
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''' Search a 2D Matrix '''
        l, r = 0, len(matrix) - 1
        while l<=r:
            mid = (l + r) // 2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif (matrix[mid][0] < target) and (matrix[mid][-1] > target):
                res = self.search(matrix[mid], target)
                return True if res > -1 else False
            # up direction
            elif matrix[mid][0] > target:
                r = mid - 1
            #down direction
            else:
                l = mid + 1
        return False

print('Binary Search')
nums, target = [-1,0,3,5,9,12], 9
# Output: 4
print(Solution().search(nums, target))
nums, target = [-1,0,3,5,9,12], 2
# Output: -1
print(Solution().search(nums, target))

print('Search a 2D Matrix')
matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13
# Output: false
print(Solution().searchMatrix(matrix, target))
matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23
# Output: true
print(Solution().searchMatrix(matrix, target))
matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34
# Output: true
print(Solution().searchMatrix(matrix, target))
