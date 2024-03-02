# https://leetcode.com/problems/valid-anagram/description/
# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        dic_t = {}
        for char in s.lower():
            if char not in dic_s:
                dic_s[char] = 0
            dic_s[char] += 1
        for char in t.lower():
            if char not in dic_t:
                dic_t[char] = 0
            dic_t[char] += 1
        return dic_s == dic_t

s, t = "anagram", "naGaram"
# s, t = "rat", "car"
# s, t = "cat", "Catherine"

Solution().isAnagram(s, t)
