# https://leetcode.com/problems/max-consecutive-ones-iii/
# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

##################
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
# 487. Max Consecutive Ones II

# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

# Example 1:
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation:
# - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
# The max number of consecutive ones is 4.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 4
# Explanation:
# - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
# The max number of consecutive ones is 4.

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, max_len, permutation = 0, 0, 0
        for i, v in enumerate(nums):
            if v == 0:
                if permutation == k:
                    while nums[l] != 0 and l < i:
                        l += 1
                    l += 1
                else:
                    permutation += 1
                    max_len = max(max_len, i - l + 1)
            else:
                max_len = max(max_len, i - l + 1)
            # print('i, l, max_len, permutation',i, l, max_len, permutation)
        return max_len

nums, k = [1,1,1,0,0,0,1,1,1,1,0], 2
# Output: 6
nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3
# Output: 10
Solution().longestOnes(nums, k)
############
nums = [1,0,1,1,0]
# Output: 4
nums = [1,0,1,1,0,1]
# Output: 4
Solution().longestOnes(nums, 1)
