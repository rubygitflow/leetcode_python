# https://leetcode.com/problems/advantage-shuffle/description/
# 870. Advantage Shuffle

# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
# Return any permutation of nums1 that maximizes its advantage with respect to nums2.

# Example 1:
# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]

# Constraints:
# 1 <= nums1.length <= 105
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 109

from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) != len(nums2):
            return []
        nums1.sort()
        t = sorted((v, i) for i, v in enumerate(nums2))
        # print('t',t)
        n = len(nums2)
        output = [0] * n
        l, r = 0, n - 1
        for v in nums1:
            if v <= t[l][0]:
                output[t[r][1]] = v
                r -= 1
            else:
                output[t[l][1]] = v
                l += 1
            # print('output',output)
        return output

if __name__ == "__main__":
    print(Solution().advantageCount([2,7,11,15], [1,10,4,11]))
    # Output: [2,11,7,15]
    print(Solution().advantageCount([12,24,8,32], [13,25,32,11]))
    # Output: [24,32,8,12]
    print(Solution().advantageCount([12,24,8], [13,25,32,11]))
    # Output: []
