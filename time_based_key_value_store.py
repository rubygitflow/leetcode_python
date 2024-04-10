# https://leetcode.com/problems/time-based-key-value-store/
# 981. Time Based Key-Value Store
# Look at binary_search.py

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

# Example 1:
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"

# Constraints:
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

from collections import defaultdict
from typing import List, Tuple

class TimeMap:
    ''' Time Based Key-Value Store '''
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self._search(key, timestamp)
        
    def _search(self, key: str, target: int) -> int:
        ''' Binary Search approximately '''
        bs_sourse = self.store[key]
        output = ''
        if bs_sourse is None:
            return output
        l, r = 0, len(bs_sourse) - 1
        while l<=r:
            mid = (l + r) // 2
            if bs_sourse[mid][0] == target:
                return bs_sourse[mid][1]
            #left direction
            elif bs_sourse[mid][0] > target:
                r = mid - 1
            #right direction
            else:
                l = mid + 1
                # remember the last known value
                output = bs_sourse[mid][1]
        #ends when r < l
        return output


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
commands = ["get", "set", "get", "get", "set", "get", "get"]
resources = [["foo", 1], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [None, "bar", "bar", None, "bar2", "bar2"]
for com, inp in zip(commands, resources):
    if com == 'set':
        output = obj.set(inp[0],inp[1],inp[2])
        print(output)
    else:
        param_2 = obj.get(inp[0],inp[1])
        print(param_2)

