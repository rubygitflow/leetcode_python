# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/
# 2006. Count Number of Pairs With Absolute Difference K
# Look at "longest_consecutive_sequence.py"

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.

# Example 1:
# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]

# Example 2:
# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.

# Example 3:
# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 1 <= k <= 99

#######################
# Take Pairs With Absolute Difference K (enumeration)

from collections import Counter
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ''' Count Number of Pairs With Absolute Difference K '''
        output = 0
        counter = Counter(nums)
        # counter = {}
        # for i in nums:
        #     if i in counter:
        #         counter[i] +=1
        #     else:
        #         counter[i] = 1
        # setter = counter.keys()
        # for v in setter:
        #     if (v + k) in setter:
        for v in counter:
            if (v + k) in counter:
                output += counter[v] * counter[v + k]
        return output
    def countKDifferenceII(self, nums: List[int], k: int) -> int:
        ''' Count Number of Pairs With Absolute Difference K (enumeration) '''
        n = len(nums)
        return sum(
            abs(nums[i] - nums[j]) == k for i in range(n) for j in range(i + 1, n)
        )
    def takeKDifference(self, nums: List[int], k: int) -> int:
        ''' Take Pairs With Absolute Difference K (enumeration) '''
        n = len(nums)
        return [[nums[i], nums[j]] for i in range(n) for j in range(i + 1, n) if abs(nums[i] - nums[j]) == k]

nums, k = [1,2,2,1], 1
# Output: 4
# Output: [[1, 2], [1, 2], [2, 1], [2, 1]]
nums, k = [1,3], 3
# Output: 0
# Output: []
nums, k = [3,2,1,5,4], 2
# Output: 3
# Output: [[3, 1], [3, 5], [2, 4]]
Solution().countKDifference(nums, k)
Solution().countKDifferenceII(nums, k)
Solution().takeKDifference(nums, k)
