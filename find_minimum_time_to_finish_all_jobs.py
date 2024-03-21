# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/description/
# 1723. Find Minimum Time to Finish All Jobs

# You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
# There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
# Return the minimum possible maximum working time of any assignment.

# Example 1:
# Input: jobs = [3,2,3], k = 3
# Output: 3
# Explanation: By assigning each person one job, the maximum time is 3.
# Example 2:
# Input: jobs = [1,2,4,7,8], k = 2
# Output: 11
# Explanation: Assign the jobs the following way:
# Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
# Worker 2: 4, 7 (working time = 4 + 7 = 11)
# The maximum working time is 11.

# Constraints:
# 1 <= k <= jobs.length <= 12
# 1 <= jobs[i] <= 107

from typing import List
from math import ceil

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        ''' Find Minimum Time to Finish All Jobs '''
        x = sorted(jobs, reverse=True)
        avg = ceil(sum(x) / k)
        baskets = [0] * k
        basket_num = 0
        while len(x) > 0:
            i = 0
            baskets[basket_num] = x.pop(i)
            avg = max(avg, baskets[basket_num])
            while i < len(x):
                if baskets[basket_num] + x[i] <= avg:
                    baskets[basket_num] += x.pop(i)
                else:
                    i += 1
            if basket_num < k - 1:
                basket_num += 1
            else:
                baskets[basket_num] += sum(x)
                x = []
        return max(baskets)

print(Solution().minimumTimeRequired([3,2,3], 3))
# Output: 3
print(Solution().minimumTimeRequired([1,2,4,7,8], 2))
# Output: 11
print(Solution().minimumTimeRequired([4,7,8], 2))
# Output: 11
