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


####################
# https://leetcode.com/problems/contains-duplicate-ii/description/
# 219. Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ''' Contains Duplicate (set)'''
        # return len(set(nums)) < len(nums)
        # No need to interate through the entire list. We return a boolean at the first duplicate
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ''' Contains Duplicate II '''
        data = dict()
        for i, num in enumerate(nums):
            if num in data and i - data[num] <= k:
                return True
            data[num] = i
        return False

print("Contains Duplicate (set)")
print(Solution().containsDuplicate([1,2,3,1]))
# Output: True
print(Solution().containsDuplicate([1,2,3,4]))
# Output: False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
# Output: True

print("Contains Duplicate II")
print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
# Output: True
print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
# Output: True
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
# Output: False
