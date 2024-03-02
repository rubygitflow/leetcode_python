# https://leetcode.com/problems/group-anagrams/description/
# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

##################
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
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [[]]
        if not strs:
            return output
        output[0].append(strs[0])
        for i in range(len(strs) - 1):
            found = False
            for elem in output:
                if self.isAnagram(strs[i + 1], elem[0]):
                    elem.append(strs[i + 1])
                    found = True
                    break
            if not found:
                output.append([strs[i + 1]])
        return output

s, t = "anagram", "naGaram"
# s, t = "rat", "car"
# s, t = "cat", "Catherine"

Solution().isAnagram(s, t)

# strs = [""]
strs = ["eat","tea","tan","ate","nat","bat"]

Solution().groupAnagrams(strs)
