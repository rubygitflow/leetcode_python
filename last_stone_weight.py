# https://leetcode.com/problems/last-stone-weight/description/
# 1046. Last Stone Weight

# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:
# Input: stones = [1]
# Output: 1

# Constraints:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

#######################
# https://leetcode.com/problems/last-stone-weight-ii/description/
# 1049. Last Stone Weight II

# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the smallest possible weight of the left stone. If there are no stones left, return 0.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

# Example 2:
# Input: stones = [31,26,33,21,40]
# Output: 5

# Constraints:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100

from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ''' Last Stone Weight (smash the heaviest two stones) '''
        while len(stones) > 1:
            u =  max(stones)
            stones.remove(u)
            v = max(stones)
            stones.remove(v)
            if (u - v) > 0:
                stones.append(u - v)
        return stones[0] if stones else 0

    def lastStoneWeightEx(self, stones: List[int]) -> int:
        ''' Last Stone Weight (smash the heaviest two stones) (heap)'''
        h = [-x for x in stones]
        heapify(h)
        while len(h) > 1:
            u, v = -heappop(h), -heappop(h)
            if v != u:
                heappush(h, v - u)
        return -h[0] if h else 0

    def lastStoneWeightII(self, stones: List[int]) -> int:
        ''' Last Stone Weight II (smash any two stones) '''
        prev_state = {0}
        for elem in stones:
            state = set()
            for prev in prev_state:
                state.add(prev + elem)
                state.add(abs(prev - elem))
            prev_state = state
        return min(prev_state)

print('Last Stone Weight')
print(Solution().lastStoneWeight([2,7,4,1,8,2]))
# Output: 0
print(Solution().lastStoneWeight([2,7,4,1,8,1]))
# Output: 1
print(Solution().lastStoneWeight([1]))
# Output: 1
print(Solution().lastStoneWeight([31,26,33,21,40]))
# Output: 9

print(Solution().lastStoneWeightEx([2,7,4,1,8,2]))
# Output: 0
print(Solution().lastStoneWeightEx([2,7,4,1,8,1]))
# Output: 1
print(Solution().lastStoneWeightEx([1]))
# Output: 1
print(Solution().lastStoneWeightEx([31,26,33,21,40]))
# Output: 9

print('Last Stone Weight II')
print(Solution().lastStoneWeightII([2,7,4,1,8,1]))
# Output: 1
print(Solution().lastStoneWeightII([31,26,33,21,40]))
# Output: 5
