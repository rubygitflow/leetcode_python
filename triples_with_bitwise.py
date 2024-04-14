# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/description/
# 982. Triples with Bitwise AND Equal To Zero

# Given an integer array nums, return the number of AND triples.
# An AND triple is a triple of indices (i, j, k) such that:
# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.

# Example 1:
# Input: nums = [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2

# Example 2:
# Input: nums = [0,0,0]
# Output: 27

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] < 216

from typing import List
from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        '''
        Triples with Bitwise AND Equal To Zero
        (Time complexity: O(n^2); Space complexity: O(max))
        '''
        cnt = Counter(x & y for x in nums for y in nums)
        return sum(v for xy, v in cnt.items() for z in nums if xy & z == 0)

    def countTripletsBF(self, nums: List[int]) -> int:
        '''
        Triples with Bitwise AND Equal To Zero (Brute Force)
        (Time complexity: O(n^3); Space complexity: O(n^3))
        '''
        return len([x for x in nums for y in nums for z in nums if x & y & z == 0])
        
print(Solution().countTriplets([2,1,3]))
# Output: 12
print(Solution().countTriplets([0,0,0]))
# Output: 27
        
print(Solution().countTripletsBF([2,1,3]))
# Output: 12
print(Solution().countTripletsBF([0,0,0]))
# Output: 27
