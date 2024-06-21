# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

########################
# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


from typing import List

class Solution:
    # Using two pointer approach
    def maxArea(self, height: List[int]) -> int:
        ''' Container With Most Water '''
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            current_area = min(height[l], height[r]) * (r - l)
            # print('left, right, current_area', height[l], height[r], current_area)
            max_area = max(max_area, current_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
    def trap(self, height: List[int]) -> int:
        ''' Trapping Rain Water '''
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        total_water = 0
        while l <= r:
            # when the left pointer has more height than left max
            # assign the left max to height at left
            # print('left, right, total_water', height[l], height[r], total_water)
            if height[l] <= height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                # if the height is less than left max
                # it means it can entrap water so adding this to total water
                else:
                    total_water += l_max - height[l]
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    total_water += r_max - height[r]
                r -= 1
        return total_water

print("Container With Most Water")
height = [1,8,6,2,5,9,8,7]
print(Solution().maxArea(height))
# Output: 49
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
# Output: 49
print(Solution().maxArea([1,1]))
# Output: 1

print("Trapping Rain Water")
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))
# Output: 6
height = [4,2,0,3,2,5]
print(Solution().trap(height))
# Output: 9
