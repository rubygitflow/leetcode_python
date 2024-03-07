# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

########################
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# 81. Search in Rotated Sorted Array II

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104

########################
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' Search in Rotated Sorted Array '''
        border = nums[0]
        if target == border:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif border < nums[mid]:  # left half is sorted
                # target is in sorted left half
                if border <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right half is sorted
                # target is in sorted right half
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    def searchII(self, nums: List[int], target: int) -> int:
        ''' Search in Rotated Sorted Array II '''
        border = nums[0]
        if target == border:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            elif border < nums[mid]:  # left half is sorted
                # target is in sorted left half
                if border <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right half is sorted
                # target is in sorted right half
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
    def findMin(self, nums: List[int]) -> int:
        ''' Find Minimum in Rotated Sorted Array '''
        if not nums:
            return None
        if len(nums) == 1 or nums[0] < nums[len(nums) - 1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        border = nums[0]
        output = border
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > border:
                l = mid + 1
            else:
                r = mid - 1
                output = min(output, nums[mid])
        return output


nums, target = [4,5,6,7,0,1,2], 0
# Output: 4
nums, target = [4,5,6,7,0,1,2], 3
# Output: -1
nums, target = [1], 0
# Output: -1
Solution().search(nums, target)

nums, target = [2,5,6,0,0,1,2], 0
# Output: true
nums, target = [2,5,6,0,0,1,2], 3
# Output: false
Solution().searchII(nums, target)

nums = [3,4,5,1,2]
# Output: 1
nums = [4,5,6,7,0,1,2]
# Output: 0
nums = [11,13,15,17]
# Output: 11
Solution().findMin(nums)
