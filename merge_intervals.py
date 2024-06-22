# https://leetcode.com/problems/merge-intervals/description/
# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        for e in sorted(intervals):
            if not output:
                output.append(e)
            else:
                l, r = output[-1]
                if e[0] <= r and e[1] >= l:
                    output[-1] = [min(e[0], l), max(e[1], r)]
                else:
                    output.append(e)
        return output


print(Solution().mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
# Output: [[1,6],[8,10],[15,18]]
intervals = [[1,3],[15,18],[2,6],[8,10]]
print(Solution().mergeIntervals(intervals))
# Output: [[1,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
print(Solution().mergeIntervals(intervals))
# Output: [[1,5]]
intervals = []
print(Solution().mergeIntervals(intervals))
# Output: []
intervals = [[-11,40],[1,4],[4,5]]
print(Solution().mergeIntervals(intervals))
# Output: [[-11,40]]
