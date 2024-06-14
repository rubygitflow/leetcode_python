# https://leetcode.com/problems/contains-duplicate/description/
# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from collections import Counter
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ''' Contains Duplicate (set)'''
        # return len(set(nums)) < len(nums)
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False

print(Solution().containsDuplicate([1,2,3,1]))
# Output: True
print(Solution().containsDuplicate([1,2,3,4]))
# Output: False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
# Output: True
