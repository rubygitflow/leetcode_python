# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
# 1578. Minimum Time to Make Rope Colorful

# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.

# Example 1:
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.

# Example 2:
# Input: colors = "abc", neededTime = [1,2,3]
# Output: 0
# Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

# Example 3:
# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

# Constraints:
# n == colors.length == neededTime.length
# 1 <= n <= 105
# 1 <= neededTime[i] <= 104
# colors contains only lowercase English letters.

from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ''' Minimum Time to Make Rope Colorful '''
        def remove(acc):
            acc.remove(max(acc))
            return sum(acc)
        if len(colors) != len(neededTime):
            return -1
        acc = [neededTime[0]]
        output = 0
        for i in range(1,len(colors)):
            if colors[i] == colors[i-1]:
                acc.append(neededTime[i])
            else:
                if len(acc) > 1:
                    output += remove(acc)
                acc = [neededTime[i]]
        if len(acc) > 1:
            output += remove(acc)
        return output
    def minCostEx(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        l = len(colors)
        if l != len(neededTime):
            return -1
        for i in range(1, l):
            if colors[i] == colors[i - 1]:
                time += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return time

print(Solution().minCost(
  "abaacs",
  [1,2,3,4,5]
))
# Output: -1
print(Solution().minCost(
  "abaac",
  [1,2,3,4,5]
))
# Output: 3
print(Solution().minCost(
  "abc",
  [1,2,3]
))
# Output: 0
print(Solution().minCost(
  "aabaa",
  [1,2,3,4,1]
))
# Output: 2
print(Solution().minCost(
  "abaaac",
  [1,2,3,4,1,5]
))
# Output: 4

print(Solution().minCostEx(
  "abaacs",
  [1,2,3,4,5]
))
# Output: -1
print(Solution().minCostEx(
  "abaac",
  [1,2,3,4,5]
))
# Output: 3
print(Solution().minCostEx(
  "abc",
  [1,2,3]
))
# Output: 0
print(Solution().minCostEx(
  "aabaa",
  [1,2,3,4,1]
))
# Output: 2
print(Solution().minCostEx(
  "abaaac",
  [1,2,3,4,1,5]
))
# Output: 4
