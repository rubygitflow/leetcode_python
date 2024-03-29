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

#######################
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/
# 1736. Latest Time by Replacing Hidden Digits

# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).
# The valid times are those inclusively between 00:00 and 23:59.
# Return the latest valid time you can get from time by replacing the hidden digits.

# Example 1:
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
# Example 2:
# Input: time = "0?:3?"
# Output: "09:39"
# Example 3:
# Input: time = "1?:22"
# Output: "19:22"

# Constraints:
# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.

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
                return time[:4] + str(to_what)
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
    def maximumTime(self, time: str) -> str:
        ''' Return the latest valid time you can get from time by replacing the hidden digits. '''
        t = list(time)
        if t[0] == '?':
            t[0] = '1' if '4' <= t[1] <= '9' else '2'
        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return ''.join(t)

timePoints = ["00:00","23:59","00:00"]
# Output: 0
print(Solution().findMinDifference(timePoints))
timePoints = ["23:59","00:00"]
# Output: 1
print(Solution().findMinDifference(timePoints))
timePoints = ["13:59","04:31"]
# Output: 568
print(Solution().findMinDifference(timePoints))

time = "19:34"
# Output: "19:39"
# print(Solution().nextClosestTimeEX(time))
print(Solution().nextClosestTime(time))
time = "23:59"
# Output: "22:22"
# print(Solution().nextClosestTimeEX(time))
print(Solution().nextClosestTime(time))

time = "2?:?0"
# Output: "23:50"
print(Solution().maximumTime(time))
time = "0?:3?"
# Output: "09:39"
print(Solution().maximumTime(time))
time = "1?:22"
# Output: "19:22"
print(Solution().maximumTime(time))
