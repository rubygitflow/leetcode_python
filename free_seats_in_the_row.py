# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
# 849. Maximize Distance to Closest Person

# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
# Return that maximum distance to the closest person.

# Example 1:
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.

# Example 2:
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.

# Example 3:
# Input: seats = [0,1]
# Output: 1

# Constraints:
# 2 <= seats.length <= 2 * 104
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.

# Free seats in the row
# Свободные места в ряду
# Определить, на каком максимальном расстоянии от посетителей можно сесть в ряду.
# [1,0,0,1]
# # Output: 1
# [1,0,0,1,0,0,0,0,1]
# # Output: 2
# [1,1,0,1,1,0,0,0,1]
# # Output: 2
# [1,1,0,1,1,0,0,0,0]
# # Output: 4

from typing import List

class Solution:
    def takeFreeSeat(self, row: List[int]) -> int:
        ''' Free seats in the row '''
        if not row:
            return 0
        l, max_dist = 0, 0
        for r, p in enumerate(row):
            if p == 0:
                if row[l] != row[r]:
                    l = r
                if r == len(row) - 1:
                   max_dist = max(max_dist, r - l + 1)
            else:
                if r == l:
                    continue 
                if row[l] != row[r]:
                    if l == 0:
                        max_dist = r - l
                    else:
                        total = r - l
                        if total % 2 == 0:
                            max_dist = max(max_dist, total // 2)
                        else:
                            max_dist = max(max_dist, total // 2 + 1)
                    l = r
        return max_dist
    def maxDistToClosest(self, seats: List[int]) -> int:
        ''' Maximize Distance to Closest Person '''
        first = last = None
        d = 0
        for i, c in enumerate(seats):
            if c:
                if last is not None:
                    d = max(d, i - last)
                if first is None:
                    first = i
                last = i
        return max(first, len(seats) - last - 1, d // 2)

r = [1,0,0,1]
# Output: 1
r = [1,0,0,1,0,0,0,0,1]
# Output: 2
r = [1,1,0,1,1,0,0,0,1]
# Output: 2
r = [1,1,0,1,1,0,0,0,0]
# Output: 4
r = [0,0,0,0]
# Output: 4
r = [0,0,0,1]
# Output: 3
Solution().takeFreeSeat(r)
Solution().maxDistToClosest(r)
