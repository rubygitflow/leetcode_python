# https://leetcode.com/problems/sliding-window-median/
# 480. Sliding Window Median

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation: 
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7        3
#  1  3  -1  -3 [5  3  6] 7        5
#  1  3  -1  -3  5 [3  6  7]       6

# Example 2:
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

# Constraints:
# 1 <= k <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

#######################
# https://leetcode.com/problems/sliding-window-maximum/description/
# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ''' Sliding Window Median '''
        res = []
        if len(nums) < k:
            return res
        odd = True if k % 2 == 1 else False
        median_index = k // 2 if odd else k // 2 - 1
        median_index_next = median_index + 1
        window = nums[:k]
        window.sort()
        for i in range(k, len(nums)):
            if odd:
                median = window[median_index]
            else:
                median = (window[median_index] + window[median_index_next]) / 2
            res.append(float(median))
            window.remove(nums[i - k])
            window.append(nums[i])
            window.sort()
        # Process the last window
        if odd:
            median = window[median_index]
        else:
            median = (window[median_index] + window[median_index_next]) / 2
        res.append(float(median))
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Sliding Window Maximum
        (Time complexity: O(n)<=T<O(n^2); Space complexity: O(k))
        https://proglib.io/p/slozhnost-algoritmov-i-operaciy-na-primere-python-2020-11-03
        '''
        res = []
        window = nums[:k]
        for i in range(k, len(nums)):
            res.append(max(window))
            window.remove(nums[i - k])
            window.append(nums[i])
        # Process the last window
        res.append(max(window))
        return res

    def maxSlidingWindowEx(self, nums: List[int], k: int) -> List[int]:
        ''' Sliding Window Maximum (short code) '''
        return [ max(nums[(i - k):i]) for i in range(k, len(nums)+1) ]

print("Sliding Window Median")
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
print(Solution().medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3))
# Output: [2, 3, 3, 3, 2, 3, 2]
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 4))
# Output: [0.0, 1.0, 1.0, 4.0, 5.5]
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 1))
# Output: [1,3,-1,-3,5,3,6,7]
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 10))
# Output: []

print("Sliding Window Maximum")
nums, size = [1,3,-1,-3,5,3,6,7], 3
# Output: [3,3,5,5,6,7]
print(Solution().maxSlidingWindow(nums, size))

print(Solution().maxSlidingWindowEx([1,3,-1,-3,5,3,6,7], 3))

