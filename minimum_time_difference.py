# https://leetcode.com/problems/minimum-time-difference/description/
# 539. Minimum Time Difference

# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1

# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0

# Constraints:
# 2 <= timePoints.length <= 2 * 104
# timePoints[i] is in the format "HH:MM".

# from itertools import pairwise
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ''' Minimum Time Difference '''
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        mins.append(mins[0] + 24 * 60) # make it a circle, linking 1st and last slot
        # return min(abs(a - b) for a, b in pairwise(mins))
        output = mins[-1]
        for i in range(1, len(mins)):
            output = min(output, mins[i] - mins[i - 1])
        return output

timePoints = ["00:00","23:59","00:00"]
# Output: 0
timePoints = ["23:59","00:00"]
# Output: 1
timePoints = ["13:59","04:31"]
# Output: 568
Solution().findMinDifference(timePoints)


