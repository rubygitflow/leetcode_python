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

##################
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# 438. Find All Anagrams in a String

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 
# Constraints:
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' Valid Anagram '''
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
        ''' Group Anagrams '''
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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ''' Find All Anagrams in a String '''
        output = []
        for i in range(len(s) - len(p) + 1):
            if self.isAnagram(s[i:i + len(p)], p):
                output.append(i)
        return output

s, t = "anagram", "naGaram"
# s, t = "rat", "car"
# s, t = "cat", "Catherine"

Solution().isAnagram(s, t)

# strs = [""]
strs = ["eat","tea","tan","ate","nat","bat"]

Solution().groupAnagrams(strs)

# s, p = "abab", "ab"
s, p = "cbaebabacd", "abc"

Solution().findAnagrams(s, p)
