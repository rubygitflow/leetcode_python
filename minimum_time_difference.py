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

#######################
# https://leetcode.com/problems/next-closest-time/description/
# 681. Next Closest Time

# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

# Example 1:
# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

# Constraints:
# time.length == 5
# time is a valid time in the form "HH:MM".
# 0 <= HH < 24
# 0 <= MM < 60

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
    def nextClosestTime(self, time: str) -> str:
        ''' Next Closest Time: digit-by-digit search for values '''
        digit_arr = [int(digit) for digit in list(time) if digit != ':']
        sorted_arr = sorted(digit_arr)
        m = digit_arr[-1]
        for to_what in sorted_arr:
            if to_what > m:
                return time[:4] + to_what
        min_dig = str(sorted_arr[0])
        mm = digit_arr[-2]
        for to_what in sorted_arr:
            if mm < to_what < 7:
                return time[:3] + str(to_what) + min_dig
        h = digit_arr[1]
        for to_what in sorted_arr:
            if h < to_what and digit_arr[0] * 10 + to_what < 24:
                return time[0] + str(to_what) + ':' + min_dig * 2
        hh = digit_arr[0]
        for to_what in sorted_arr:
            if hh < to_what and to_what * 10 + sorted_arr[0] < 24:
                return str(to_what) + min_dig + ':' + min_dig * 2
        return min_dig * 2 + ':' + min_dig * 2
    def nextClosestTimeEX(self, time: str) -> str:
        ''' Next Closest Time: minute-by-minute search for values '''
        h, m = time.split(":")
        curr = int(h) * 60 + int(m)
        result = None
        # в диапазоне от текущего времени и до через сутки
        for i in range(curr+1, curr+1441):
            t = i % 1440
            h, m = t // 60, t % 60
            result = "%02d:%02d" % (h, m)
            if set(result) <= set(time):
                break
        return result

timePoints = ["00:00","23:59","00:00"]
# Output: 0
timePoints = ["23:59","00:00"]
# Output: 1
timePoints = ["13:59","04:31"]
# Output: 568
Solution().findMinDifference(timePoints)

time = "19:34"
# Output: "19:39"
time = "23:59"
# Output: "22:22"
Solution().nextClosestTime(time)
Solution().nextClosestTimeEX(time)
