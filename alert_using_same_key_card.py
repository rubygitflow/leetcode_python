# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/description/
# 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period

# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

# Example 1:
# Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# Output: ["daniel"]
# Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
# Example 2:
# Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# Output: ["bob"]
# Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

# Constraints:
# 1 <= keyName.length, keyTime.length <= 105
# keyName.length == keyTime.length
# keyTime[i] is in the format "HH:MM".
# [keyName[i], keyTime[i]] is unique.
# 1 <= keyName[i].length <= 10
# keyName[i] contains only lowercase English letters.

from collections import defaultdict
from typing import List

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ''' Alert Using Same Key-Card Three or More Times in a One Hour Period '''
        d = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            t = int(t[:2]) * 60 + int(t[3:])
            d[name].append(t)
        output = []
        for name, ts in d.items():
            if (n := len(ts)) > 2:
                ts.sort()
                for i in range(n - 2):
                    if ts[i + 2] - ts[i] <= 60:
                        output.append(name)
                        break
        output.sort()
        return output

print(Solution().alertNames(
  ["daniel","daniel","daniel","luis","luis","luis","luis"],
  ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
))
# Output: ["daniel"]
print(Solution().alertNames(
  ["alice","alice","alice","bob","bob","bob","bob"],
  ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
))
# Output: ["bob"]
