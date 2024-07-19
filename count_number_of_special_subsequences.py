# https://leetcode.com/problems/count-number-of-special-subsequences/
# 1955. Count Number of Special Subsequences
# Explanation: https://algo.monster/liteproblems/1955

# A sequence is special if it consists of a positive number of 0s, followed by a positive number of 1s, then a positive number of 2s.
# For example, [0,1,2] and [0,0,1,1,1,2] are special.
# In contrast, [2,1,0], [1], and [0,1,2,0] are not special.
# Given an array nums (consisting of only integers 0, 1, and 2), return the number of different subsequences that are special. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are different if the set of indices chosen are different.

# Example 1:
# Input: nums = [0,1,2,2]
# Output: 3
# Explanation: The special subsequences are bolded [0,1,2,2], [0,1,2,2], and [0,1,2,2].

# Example 2:
# Input: nums = [2,2,0,0]
# Output: 0
# Explanation: There are no special subsequences in [2,2,0,0].

# Example 3:
# Input: nums = [0,1,2,0,1,2]
# Output: 7
# Explanation: The special subsequences are bolded:
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]

# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 2

from functools import reduce
from typing import List

MOD = 10**9 + 7

class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        '''
        Count Number of Special Subsequences (FOR-loop)
        подсчет перебором за один проход
        '''
        total_zeros = 0 # number of subsequences of 0s so far
        total_ones = 0 # the number of subsequences of 0s followed by 1s so far
        total_twos = 0 # the number of special subsequences so far
        for n in nums:
            if n == 0:
                # if we have found new 0 we can add it to any existing subsequence of 0s
                # or use only this 0
                total_zeros += (total_zeros + 1) % MOD
            elif n == 1:
                # if we have found new 1 we can add it to any existing subsequence of 0s or 0s and 1s
                # to get a valid subsequence of 0s and 1s
                total_ones += (total_zeros + total_ones) % MOD
            else:
                # if we have found new 2 we can add it to any existing subsequence of 0s and 1s 0r 0s,1s and 2s
                # to get a valid subsequence of 0s,1s and 2s
                total_twos += (total_ones + total_twos) % MOD
        return total_twos

    def countSpecialSubsequencesII(self, nums: List[int]) -> int:
        ''' Count Number of Special Subsequences (reduce)'''
        return reduce(lambda acc, n:\
            ((1 + 2*acc[0]) % MOD if n == 0 else acc[0],\
            (acc[0] + 2*acc[1]) % MOD if n == 1 else acc[1],\
            (acc[1] + 2*acc[2]) % MOD if n == 2 else acc[2]),\
            nums, (0,0,0))[2]


if __name__ == "__main__":
    print("Count Number of Special Subsequences (FOR-loop)")
    nums = [0,1,2]
    print(Solution().countSpecialSubsequences(nums))
    # Output: 1
    nums = [0,1,2,0]
    print(Solution().countSpecialSubsequences(nums))
    # Output: 1
    nums = [0,1,2,2]
    print(Solution().countSpecialSubsequences(nums))
    # Output: 3
    nums = [2,2,0,0]
    print(Solution().countSpecialSubsequences(nums))
    # Output: 0
    nums = [0,1,2,0,1,2]
    print(Solution().countSpecialSubsequences(nums))
    # Output: 7
    # 0 - 1 вариант
    # 00 - 2+1 варианта  0_ _0 00
    # 000 - 6 + 1 вариантов 0__ _0_ 00_ 0_0 _00 __0 000

    print("Count Number of Special Subsequences (reduce)")
    print(Solution().countSpecialSubsequencesII([0,1,2]))
    # Output: 1
    print(Solution().countSpecialSubsequencesII([0,1,2,0]))
    # Output: 1
    print(Solution().countSpecialSubsequencesII([0,1,2,2]))
    # Output: 3
    print(Solution().countSpecialSubsequencesII([2,2,0,0]))
    # Output: 0
    print(Solution().countSpecialSubsequencesII([0,1,2,0,1,2]))
    # Output: 7
