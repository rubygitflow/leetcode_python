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
    def threeSum(self, nums: List[int], target: int = 0) -> List[List[int]]:
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

nums, target = [-1,0,1,2,-1,-4], 0
print(Solution().threeSum(nums, target))
# Output: [[-1,-1,2],[-1,0,1]]
nums, target = [-2,0,1,1,2,-1,-4], 3
print(Solution().threeSum(nums, target))
# Output: [[0, 1, 2]]

print(Solution().threeSum([0,1,1]))
# Output: []
print(Solution().threeSum([0,0,0]))
# Output: [[0,0,0]]

