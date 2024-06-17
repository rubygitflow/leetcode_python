# https://leetcode.com/problems/jump-game-vii/
# 1871. Jump Game VII

# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

# Example 1:
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.

# Example 2:
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false

# Constraints:
# 2 <= s.length <= 105
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length


########################
# https://leetcode.com/problems/jump-game/description/
# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        ''' Jump Game VII '''
        def dfs(i):
            if i == len(s) - 1:
                return True
            for step in range(minJump, maxJump + 1):
                if s[i + step] == '0':
                    if dfs(i + step):
                        return True
            return False
        return dfs(0)

    def canJump(self, nums: List[int]) -> bool:
        ''' Jump Game '''
        as_far_as_possible = 0
        for i, jump in enumerate(nums):
            if as_far_as_possible < i:
                return False
            as_far_as_possible = max(as_far_as_possible, i + jump)
        return True


print("Jump Game VII")
s = "011010"
minJump = 2
maxJump = 3
print(Solution().canReach(s, minJump, maxJump))
# Output: True
s = "01101110"
minJump = 2
maxJump = 3
print(Solution().canReach(s, minJump, maxJump))
# Output: False

print("Jump Game")
print(Solution().canJump([2,3,1,1,4]))
# Output: True
print(Solution().canJump([3,2,1,0,4]))
# Output: False
