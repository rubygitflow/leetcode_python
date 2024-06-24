# https://leetcode.com/problems/single-number/
# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

#######################
# https://leetcode.com/problems/single-number-ii/description/
# 137. Single Number II

# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3

# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

# Constraints:
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.


# from functools import reduce
# https://docs-python.ru/standart-library/modul-functools-python/funktsija-reduce-modulja-functools/

from collections import Counter, defaultdict
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ''' Single Number '''
        # return reduce(lambda x, y: x ^ y, nums)
        for i in range(1, len(nums)):
            # Проводим побитовую операцию xor
            nums[0] ^= nums[i]
        return nums[0]
    def singleNumberII(self, nums: List[int]) -> int:
        '''
        Single Number II
        Approach: Magic
        Explanation
        https://leetcode.com/problems/single-number-ii/solutions/3714928/bit-manipulation-c-java-python-beginner-friendly/
        '''
        ones = 0
        twos = 0
        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)
        return ones
    def singleNumberBF(self, nums: List[int]) -> int:
        '''
        Single Number II
        Approach: Brute Force
        '''
        count = defaultdict(int)
        for x in nums:
            count[x] += 1
        for x, freq in count.items():
            if freq == 1:
                return x
        return 0
    def singleNumberBFII(self, nums: List[int]) -> int:
        '''
        Single Number II
        Approach: Brute Force with Counter
        '''
        count = Counter(nums)
        for x, freq in count.items():
            if freq == 1:
                return x
        return 0

print("Single Number")
print(Solution().singleNumber([2,2,1,1,1]))
# Output: 1
print(Solution().singleNumber([2,2,1]))
# Output: 1
print(Solution().singleNumber([4,1,2,1,2]))
# Output: 4
print(Solution().singleNumber([1]))
# Output: 1
print(Solution().singleNumber([0,1,0,1,0,1]))
# Output: 1 - couldn't resolve correctly
print(Solution().singleNumber([0,1,0,1]))
# Output: 0 - unexpected situation

print("Single Number (Brute Force)")
print(Solution().singleNumberBF([0,1,0,1,0,1,99]))
# Output: 99
print(Solution().singleNumber([0,1,0,1,0,1,99]))
# Output: 98 - couldn't resolve correctly
print(Solution().singleNumberBF([0,1,0,1,0,1]))
# Output: 0 - unexpected situation

print("Single Number II")
print(Solution().singleNumberII([2,2,3,2]))
# Output: 3
print(Solution().singleNumberII([0,1,0,1,0,1,99]))
# Output: 99
print(Solution().singleNumberII([0,1,0,1,0,1]))
# Output: 0
print("Single Number II (Brute Force)")
print(Solution().singleNumberBFII([0,1,0,1,0,1,99]))
# Output: 99
