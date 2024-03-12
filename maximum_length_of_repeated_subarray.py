# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
# 718. Maximum Length of Repeated Subarray

# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

# Example 1:
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# Example 2:
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100

from collections import defaultdict
from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ''' Maximum Length of Repeated Subarray '''
        num2_dic = defaultdict(set)
        for i, v in enumerate(nums2):
            num2_dic[v].add(i)
        max_len = 0
        for i, v in enumerate(nums1):
            if max_len > len(nums1) - 1 - i:
                return max_len
            for j in num2_dic[v]:
                loc_len = 1
                max_len = max(max_len, loc_len)
                r1, r2 = i+1, j+1
                while r1 < len(nums1) and r2 < len(nums2) and nums1[r1] == nums2[r2]:
                    loc_len += 1
                    max_len = max(max_len, loc_len)
                    r1 += 1
                    r2 += 1
        return max_len

nums1, nums2 = [1,2,3,2,1], [3,2,1,4,7]
# Output: 3
nums1, nums2 = [0,0,0,0,0], [0,0,0,0,0]
# Output: 5
Solution().findLength(nums1, nums2)
