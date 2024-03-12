# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
# 719. Find K-th Smallest Pair Distance

# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

# Example 1:
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.

# Example 2:
# Input: nums = [1,1,1], k = 2
# Output: 0

# Example 3:
# Input: nums = [1,6,1], k = 3
# Output: 5

# Constraints:
# n == nums.length
# 2 <= n <= 104
# 0 <= nums[i] <= 106
# 1 <= k <= n * (n - 1) / 2

from collections import Counter
from typing import List
from bisect import bisect_left

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        ''' Find K-th Smallest Pair Distance (Brute Force)'''
        diffs = Counter()
        for l in range(len(nums) - 1):
            for r in range(l + 1,len(nums)):
                diffs[abs(nums[r] - nums[l])] += 1
        diff_arr = sorted(diffs)
        l = -1
        count_kth_diff = 0
        for el in diff_arr:
            count_kth_diff += diffs[el]
            if count_kth_diff >= k:
                return el
        return -1
    def smallestDistancePairII(self, nums: List[int], k: int) -> int:
        ''' Find K-th Smallest Pair Distance (optimized)'''
        def count(dist):
            cnt = 0
            for i, b in enumerate(nums):
                a = b - dist
                j = bisect_left(nums, a, 0, i)
                cnt += i - j
            return cnt
        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)

nums, k = [1,3,1], 1
# Output: 0
nums, k = [1,1,1], 2
# Output: 0
nums, k = [1,6,1], 3
# Output: 5
Solution().smallestDistancePair(nums, k)
Solution().smallestDistancePairII(nums, k)
