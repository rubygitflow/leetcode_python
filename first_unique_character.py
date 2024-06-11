# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ''' First Unique Character in a String '''
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1

print(Solution().firstUniqChar("leetcode"))
# Output: 0
print(Solution().firstUniqChar("loveleetcode"))
# Output: 2
print(Solution().firstUniqChar("aabb"))
# Output: -1
