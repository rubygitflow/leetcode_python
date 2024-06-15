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


####################
# https://leetcode.com/problems/contains-duplicate-iii/description/
# 220. Contains Duplicate III

# You are given an integer array nums and two integers indexDiff and valueDiff.
# Find a pair of indices (i, j) such that:
# i != j,
# abs(i - j) <= indexDiff.
# abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.

# Example 1:
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true
# Explanation: We can choose (i, j) = (0, 3).
# We satisfy the three conditions:
# i != j --> 0 != 3
# abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
# abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

# Example 2:
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false
# Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.

# Constraints:
# 2 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 1 <= indexDiff <= nums.length
# 0 <= valueDiff <= 109


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
        visited = dict()
        for i, num in enumerate(nums):
            if num in visited and i - visited[num] <= k:
                return True

            visited[num] = i
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        ''' Contains Duplicate III '''
        if len(nums) < 2 or valueDiff < 0 or indexDiff < 1: return False

        nearby = valueDiff + 1
        visited = dict()
        for i, num in enumerate(nums):
            idx = num//nearby
            # because of rounded idx we almost verify idx-1 and idx+1
            if (idx in visited and i - visited[idx][0] <= indexDiff) or \
               (idx-1 in visited and \
                i - visited[idx-1][0] <= indexDiff and \
                abs(num - visited[idx-1][1]) <= valueDiff) or \
               (idx+1 in visited and \
                i - visited[idx+1][0] <= indexDiff and \
                abs(num - visited[idx+1][1]) <= valueDiff): return True

            visited[idx] = (i, num)
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

print("Contains Duplicate III")
print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
# Output: True
print(Solution().containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
# Output: False
