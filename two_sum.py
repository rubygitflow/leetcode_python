# https://leetcode.com/problems/two-sum/description/
# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

#######################
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000

# The tests are generated such that there is exactly one solution.

#######################
# https://leetcode.com/problems/3sum/description/
# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Two Sum '''
        num_map = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            num_map[nums[i]] = i
        return []  # No solution found
    def twoSumSorted(self, numbers: List[int], target: int) -> List[int]:
        ''' Two Sum II - Input Array Is Sorted '''
        num_map = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement]+1, i+1]
            num_map[nums[i]] = i
        return []  # No solution found
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        ''' 3Sum '''
        n = len(nums)
        if n < 3:
            return []
        # Используем set чтобы исключить дубли по l, r
        output = set()
        # сортировка нужна, чтобы исключить дубли в выходном массиве
        nums.sort()
        for i, v in enumerate(nums[:-2]):
            if i > 0 and v == nums[i-1]:
                # пропускаем дубли триплетов (по условию задачи)
                continue
            # two pointers подход
            l = i+1
            r = n-1
            current = target - v
            while l < r:
                if nums[l] + nums[r] == current:
                    output.add((v, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > current:
                    r -= 1
                else:
                    l += 1
        return list(map(list, output))

nums, target = [2,7,11,15], 9
# Output: [0,1]
Solution().twoSum(nums, target)

nums, target = [2,3,4], 6
# Output: [1,3]
Solution().twoSumSorted(nums, target)

# nums = [-1,0,1,2,-1,-4]
nums, target = [-2,0,1,1,2,-1,-4], 3
# Output: [[-1,-1,2],[-1,0,1]]
Solution().threeSum(nums, target)
