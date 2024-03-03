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

##################
# https://leetcode.com/problems/find-anagram-mappings/description/
# 760. Find Anagram Mappings

# You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1.
# Both arrays may contain duplicates
# Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j. If there are multiple answers, return any of them.
# An array a is an anagram of an array b means b is made by randomizing the order of the elements in a.

# Example 1:
# Input: nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
# Output: [1,4,3,2,0]
# Explanation: As mapping[0] = 1 because the 0th element of nums1 appears at nums2[1], and mapping[1] = 4 because the 1st element of nums1 appears at nums2[4], and so on.

# Example 2:
# Input: nums1 = [84,46], nums2 = [84,46]
# Output: [0,1]

# Constraints:
# 1 <= nums1.length <= 100
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 105
# nums2 is an anagram of nums1.

##################
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
# 1347. Minimum Number of Steps to Make Two Strings Anagram

# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:
# Input: s = "bab", t = "aba"
# Output: 1
# Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

# Example 2:
# Input: s = "leetcode", t = "practice"
# Output: 5
# Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

# Example 3:
# Input: s = "anagram", t = "mangaar"
# Output: 0
# Explanation: "anagram" and "mangaar" are anagrams. 

# Constraints:
# 1 <= s.length <= 5 * 104
# s.length == t.length
# s and t consist of lowercase English letters only.

##################
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/description/
# 2186. Minimum Number of Steps to Make Two Strings Anagram II

# You are given two strings s and t. In one step, you can append any character to either s or t.
# Return the minimum number of steps to make s and t anagrams of each other.
# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:
# Input: s = "leetcode", t = "coats"
# Output: 7
# Explanation: 
# - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
# - In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
# "leetcodeas" and "coatsleede" are now anagrams of each other.
# We used a total of 2 + 5 = 7 steps.
# It can be shown that there is no way to make them anagrams of each other with less than 7 steps.

# Example 2:
# Input: s = "night", t = "thing"
# Output: 0
# Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.

# Constraints:
# 1 <= s.length, t.length <= 2 * 105
# s and t consist of lowercase English letters.

##################
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/
# 2273. Find Resultant Array After Removing Anagrams

# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
# In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

# Example 1:
# Input: words = ["abba","baba","bbaa","cd","cd"]
# Output: ["abba","cd"]
# Explanation:
# One of the ways we can obtain the resultant array is by using the following operations:
# - Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
#   Now words = ["abba","baba","cd","cd"].
# - Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
#   Now words = ["abba","cd","cd"].
# - Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
#   Now words = ["abba","cd"].
# We can no longer perform any operations, so ["abba","cd"] is the final answer.

# Example 2:
# Input: words = ["a","b","c","d","e"]
# Output: ["a","b","c","d","e"]
# Explanation:
# No two adjacent strings in words are anagrams of each other, so no operations are performed.

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.

from typing import Dict
from typing import List
from collections import Counter, defaultdict

class Solution:
    def __dictFromString(self, s: str) -> Dict:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        return d
    def isAnagramOld(self, s: str, t: str) -> bool:
        ''' Valid Anagram (Old Version - Case sensitive) '''
        if len(s) != len(t):
            return False
        return self.__dictFromString(s) == self.__dictFromString(t)
    def isAnagram(self, s: str, t: str) -> bool:
        ''' Valid Anagram '''
        if len(s) != len(t):
            return False
        # dic_s = {}
        # for char in s.lower():
        #     if char not in dic_s:
        #         dic_s[char] = 0
        #     dic_s[char] += 1
        dic_s = Counter(s.lower())
        # dic_t = {}
        # for char in t.lower():
        #     if char not in dic_t:
        #         dic_t[char] = 0
        #     dic_t[char] += 1
        dic_t = Counter(t.lower())
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
    def minSteps(self, s: str, t: str) -> int:
        ''' Minimum Number of Steps to Make Two Strings Anagram '''
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
        output = 0
        for key in dic_t:
            if key in dic_s:
                difference = dic_t[key] - dic_s[key]
                if difference > 0:
                    output += difference
            else:
                output += dic_t[key]
        return output
    def minStepsII(self, s: str, t: str) -> int:
        ''' Minimum Number of Steps to Make Two Strings Anagram II '''
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
        output = 0
        for key in dic_t:
            if key in dic_s:
                difference = abs(dic_t[key] - dic_s[key])
                output += difference
                dic_s.pop(key)
            else:
                output += dic_t[key]
        for key in dic_s:
            output += dic_s[key]
        return output
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ''' Find Anagram Mappings '''
        mapper = defaultdict(set)
        for i, num in enumerate(nums2):
            mapper[num].add(i)
        return [mapper[num].pop() for num in nums1]
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ''' Find Resultant Array After Removing Anagrams '''
        return [
            w
            for i, w in enumerate(words)
            if i == 0 or sorted(w) != sorted(words[i - 1])
        ]

s, t = "anagram", "naGaram"
# Output: True
# s, t = "rat", "car"
# s, t = "cat", "Catherine"
Solution().isAnagram(s, t)
s, t = "anagram", "margana"
# Case sensitive!!!
Solution().isAnagramOld(s, t)

# strs = [""]
strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
Solution().groupAnagrams(strs)

# s, p = "abab", "ab"
s, p = "cbaebabacd", "abc"
# Output: [0, 6]
Solution().findAnagrams(s, p)

s, t = "leetcode", "practice"
# Output: 5
# s, t = "bab", "aba"
# s, t = "anagram", "mangaar"
Solution().minSteps(s, t)

# s, t = "leetcode", "coats"
s, t = "night", "thing"
# Output: 0
Solution().minStepsII(s, t)

# nums1 = [12,28,46,32,50]
# nums2 = [50,12,32,46,28]
# Output: [1,4,3,2,0]

# nums1 = [84,46]
# nums2 = [84,46]
# Output: [0,1]

nums1 = [84,46,46]
nums2 = [46,84,46]
# Output: [1, 0, 2]
Solution().anagramMappings(nums1, nums2)

# words = ["abba","baba","bbaa","cd","cd"]
# Output: ['abba', 'cd']
words = ["abba","bbaa","cd","cd","baba"]
# Output: ['abba', 'cd', 'baba']
Solution().removeAnagrams(words)
