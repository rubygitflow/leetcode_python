# https://leetcode.com/problems/largest-time-for-given-digits/description/
# 949. Largest Time for Given Digits

# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

# Example 1:
# Input: arr = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

# Example 2:
# Input: arr = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.

# Constraints:
# arr.length == 4
# 0 <= arr[i] <= 9

from itertools import permutations
from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ''' Largest Time for Given Digits '''
        def minute_first_digit(arr,res):
            return res+str(arr[0])
        def minute_second_digit(arr,res):
            out = ''
            for i in range(5, -1, -1):
                if i in arr:
                    pos = arr.index(i)
                    arr.remove(i)
                    out = minute_first_digit(arr, res+str(i))
                    break
            return out
        def hour_first_digit(arr,res):
            out = ''
            for i in range(3 if res == '2' else 9, -1, -1):
                if i in arr:
                    pos = arr.index(i)
                    arr.remove(i)
                    out = minute_second_digit(arr, res+str(i)+':')
                    break
            return out
        out = ''
        for i in range(2, -1, -1):
            if i in arr:
                pos = arr.index(i)
                arr.remove(i)
                out = hour_first_digit(arr,str(i))
                break
        return out
    def largestTimeFromDigitsEx(self, A: List[int]) -> str:
        ''' Largest Time for Given Digits (with permutations)'''
        arr = list(permutations(sorted(A, reverse=True)))
        for h1, h2, m1, m2 in arr:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                return f'{h1}{h2}:{m1}{m2}'
        return ''
    def largestTimeFromDigitsBF(self, A: List[int]) -> str:
        ''' Largest Time for Given Digits (Brute Force)'''
        # From 23:59 to 00:00 go over every minute of 24 hours. If A meets this requirement, then totaly 24 * 60 minutes. Since using sort during the ongoing judegment process, so the time complexity is low.
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h//10, h % 10, m // 10, m % 10]
                ts = sorted(t)
                if ts == A:
                    return str(t[0]) + str(t[1]) +':' + str(t[2]) + str(t[3])
        return ''

print('Largest Time for Given Digits')
print(Solution().largestTimeFromDigits([1,5,3,4]))
# Output: "15:43"
print(Solution().largestTimeFromDigits([1,2,3,4]))
# Output: "23:41"
print(Solution().largestTimeFromDigits([5,5,5,5]))
# Output: ""
print(Solution().largestTimeFromDigits([0,9,9,9]))
# Output: ""

print('Largest Time for Given Digits (with permutations)')
print(Solution().largestTimeFromDigitsEx([1,5,3,4]))
# Output: "15:43"
print(Solution().largestTimeFromDigitsEx([1,2,3,4]))
# Output: "23:41"
print(Solution().largestTimeFromDigitsEx([5,5,5,5]))
# Output: ""
print(Solution().largestTimeFromDigitsEx([0,9,9,9]))
# Output: ""

print('Largest Time for Given Digits (Brute Force)')
print(Solution().largestTimeFromDigitsBF([1,5,3,4]))
# Output: "15:43"
print(Solution().largestTimeFromDigitsBF([1,2,3,4]))
# Output: "23:41"
print(Solution().largestTimeFromDigitsBF([5,5,5,5]))
# Output: ""
print(Solution().largestTimeFromDigitsBF([0,9,9,9]))
# Output: ""
