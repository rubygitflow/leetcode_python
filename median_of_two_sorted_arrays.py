# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# a bad, naive solution  - O(N * log N)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ''' Median of Two Sorted Arrays '''
        list3 = nums1 + nums2
        list3.sort()
        l = len(list3)
        k = l // 2
        if (l % 2) == 0:
            (list3[k] + list3[k-1]) / 2
        else:
            list3[k]

# a good, optimized solution  - O(log (m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ''' Median of Two Sorted Arrays '''
        if len(nums1) < len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
        # Initialization
        la, lb = len(a), len(b)
        l, r = 0, la - 1
        half = (la + lb) // 2
        # Binary search loop
        while True:
            i = (l + r) // 2  # Partition position in 'a'
            j = half - i - 2  # Complementary partition position in 'b'
            # Handling edge cases with '-inf' and 'inf'
            a_current = a[i] if i >= 0 else float('-inf')
            a_right = a[i + 1] if i + 1 < la else float('inf')
            b_current = b[j] if j >= 0 else float('-inf')
            b_right = b[j + 1] if j + 1 < lb else float('inf')
            # Check if correct partition is found
            if a_current <= b_right and b_current <= a_right:
                # Handle odd combined length
                if (la + lb) % 2:
                    return min(a_right, b_right)
                # Handle even combined length
                else:
                    return (max(a_current, b_current) + min(a_right, b_right)) / 2
            elif a_current > b_right:
                r = i - 1  # Move partition in 'a' left
            else: # b_current > a_right
                l = i + 1  # Move partition in 'a' right


# Input:
# 1)
# nums1 = [3, 19, 20] 
# nums2 = [1, 5] 
# 2)
# nums1 = [19, 20] 
# nums2 = [1, 3, 5, 20] 
# 3)
# nums1 = [1, 3, 5, 7, 9]     
# nums2 = [0, 3, 4, 5, 6]  
# 4)
# nums1 = [1, 3, 4, 5, 7, 9]     
# nums2 = [0, 3, 4, 5, 6]  
# 5)
# nums1 = [11, 13, 15, 17, 19] 
# nums2 = [0, 3, 4, 5, 6]   
# 6)
# nums1 = [11, 13, 15, 17, 19, 20] 
# nums2 = [0, 3, 4, 5, 6]  
# 7)
# nums1 = [19, 20] 
# nums2 = [0, 3, 4, 5, 6]  
# 8)
# nums1 = [19, 20] 
# nums2 = [0, 3, 4, 5, 6, 16]     
# 9)
# nums1 = [19, 20, 21] 
# nums2 = [0, 3, 4, 5, 6]    
# 10)
# nums1 = [] 
# nums2 = [0, 3, 4, 5, 6]   
# 11)
nums1 = [3, 19, 20] 
nums2 = [] 

# Execute:
Solution().findMedianSortedArrays(nums1, nums2)
