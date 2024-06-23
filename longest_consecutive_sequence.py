# https://leetcode.com/problems/longest-consecutive-sequence/description/
# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        srt = set(nums)
        max_arr = 0
        for x in nums:
            # находим минимум будущей последовательности
            if x - 1 not in srt:
                # учитываем размерность последовательности из одного числа
                y = x + 1
                # находим максимум искомой последовательности
                while y in srt:
                    y += 1
                max_arr = max(max_arr, y - x)
        return max_arr

print(Solution().longestConsecutive([100,4,200,1,3,2]))
# Output: 4
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# Output: 9
print(Solution().longestConsecutive([0,3,17,12,5,8,14,26,0,21]))
# Output: 1
