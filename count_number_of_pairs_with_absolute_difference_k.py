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

#######################
# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
# 532. K-diff Pairs in an Array

# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
# Notice that |val| denotes the absolute value of val.

# Example 1:
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Example 3:
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Constraints:
# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107

from collections import Counter
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ''' Count Number of Pairs With Absolute Difference K '''
        output = 0
        counter = Counter(nums)
        # Instead of:
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
    def findPairs(self, nums: List[int], k: int) -> int:
        ''' K-diff Pairs in an Array '''
        backside, output = set(), set()
        for v in nums:
            if v - k in backside:
                output.add(v - k)
            if v + k in backside:
                output.add(v)
            backside.add(v)
        return len(output)
    def findPairsII(self, nums: List[int], k: int) -> int:
        ''' K-diff Pairs in an Array (short)'''
        set_array = Counter(nums)
        if k == 0:
            return len([v for i, v in enumerate(set_array) if set_array[i] > 1])
        return len(set([v for i, v in enumerate(nums) if v + k in set_array]))
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

nums, k = [3,1,4,1,5], 2
# Output: 2
nums, k = [1,2,3,4,5], 1
# Output: 4
nums, k = [1,3,1,5,4], 0
# Output: 1
Solution().findPairs(nums, k)
Solution().findPairsII(nums, k)
