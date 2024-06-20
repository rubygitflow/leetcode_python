# https://leetcode.com/problems/longest-common-prefix/description/
# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ''' Longest Common Prefix '''
        if len(strs) < 2: return ""

        for i, char in enumerate(strs[0]):
            for word in strs[1:]:
                if len(word)<=i or word[i] != char:
                    return strs[0][:i]
        return strs[0]

print("Longest Common Prefix")
print(Solution().longestCommonPrefix(["flower","flow","flight"]))
# Output: "fl"
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
# Output: ""
print(Solution().longestCommonPrefix(["flow","flow","flow"]))
# Output: "flow"
print(Solution().longestCommonPrefix(["dog"]))
# Output: ""
