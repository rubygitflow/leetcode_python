# https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/description/
# 2863. Maximum Length of Semi-Decreasing Subarrays

# You are given an integer array nums.
# Return the length of the longest semi-decreasing subarray of nums, and 0 if there are no such subarrays.
# A subarray is a contiguous non-empty sequence of elements within an array.
# A non-empty array is semi-decreasing if its first element is strictly greater than its last element.

# Example 1:
# Input: nums = [7,6,5,4,3,2,1,6,10,11]
# Output: 8
# Explanation: Take the subarray [7,6,5,4,3,2,1,6].
# The first element is 7 and the last one is 6 so the condition is met.
# Hence, the answer would be the length of the subarray or 8.
# It can be shown that there aren't any subarrays with the given condition with a length greater than 8.

# Example 2:
# Input: nums = [57,55,50,60,61,58,63,59,64,60,63]
# Output: 6
# Explanation: Take the subarray [61,58,63,59,64,60].
# The first element is 61 and the last one is 60 so the condition is met.
# Hence, the answer would be the length of the subarray or 6.
# It can be shown that there aren't any subarrays with the given condition with a length greater than 6.

# Example 3:
# Input: nums = [1,2,3,4]
# Output: 0
# Explanation: Since there are no semi-decreasing subarrays in the given array, the answer is 0.

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from collections import defaultdict
from typing import List

inf = float('inf')

class Solution:
    def maxSubarrayLengthDec(self, nums: List[int]) -> int:
        ''' Maximum Length of Semi-Decreasing Subarrays '''
        # print('nums',nums)
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        # print('d',d)
        # print('reverse_sorted(d)',sorted(d, reverse=True))
        ans, k = 0, inf
        for x in sorted(d, reverse=True):
            ans = max(ans, d[x][-1] - k + 1)
            k = min(k, d[x][0])
            # print('x',x,'ans',ans,'k',k)
        return ans
    def maxSubarrayLengthInc(self, nums: List[int]) -> int:
        ''' Maximum Length of Semi-Increasing Subarrays '''
        # print('nums',nums)
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        # print('d',d)
        # print('sorted(d)',sorted(d))
        ans, k = 0, inf
        for x in sorted(d):
            ans = max(ans, d[x][-1] - k + 1)
            k = min(k, d[x][0])
            # print('x',x,'ans',ans,'k',k)
        return ans

print("Semi-Decreasing Subarrays")
print(Solution().maxSubarrayLengthDec([7,6,5,4,3,2,1,6,10,11]))
# Output: 8
print(Solution().maxSubarrayLengthDec([57,55,50,60,61,58,63,59,64,60,63]))
# Output: 6
print(Solution().maxSubarrayLengthDec([57,55,50,60,61,58,63,59,64,58,63]))
# Output: 7
print(Solution().maxSubarrayLengthDec([1,2,3,4]))
# Output: 0
print(Solution().maxSubarrayLengthDec([10,12,12,11,11]))
# Output: 4

print("Semi-Increasing Subarrays")
print(Solution().maxSubarrayLengthInc([11,10,6,1,2,3,4,5,6,7]))
# Output: 8
print(Solution().maxSubarrayLengthInc([63,59,64,60,63,55,57,50,60,61,58,]))
# Output: 9
print(Solution().maxSubarrayLengthInc([57,55,50,60,61,58,63,59,64,58,63]))
# Output: 11
print(Solution().maxSubarrayLengthInc([1,2,3,4]))
# Output: 4
print(Solution().maxSubarrayLengthInc([101,92,53,4]))
# Output: 0
print(Solution().maxSubarrayLengthInc([11,11,12,12,10]))
# Output: 4
