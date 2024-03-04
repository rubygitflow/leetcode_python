# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from typing import Dict
from typing import List

class Solution:
    ''' Парсер строк на уникальные последовательсноти '''
    dictArray = {}
    def lengthOfLongestSubstring(self, s: str) -> int:
        ''' извлечение из строки подстрок с последовательностью уникальных символов '''
        self.dictArray = {}
        maxLength = 0
        # charSet = {} # https://www.w3schools.com/python/python_dictionaries.asp
        charSet = set() # https://www.w3schools.com/python/python_sets.asp
        l = 0
        for r in range(len(s)):
            if s[r] not in charSet:
                # запоминаем
                charSet.add(s[r])
                maxLength = max(maxLength, r - l + 1)
                self.dictArray[l] = s[l:r+1]
            else:
                # слишком грубое обрезание
                # charSet.clear()
                # l = r
                # мягкое удаление слева до уникального символа
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                # продолжаем запоминание
                charSet.add(s[r])
                self.dictArray[l] = s[l:r+1]
        return maxLength
    def fetchListsByLength(self, length: int) -> List[str]:
        ''' список строк заданной длины из словаря dictArray '''
        output = []
        for elem in self.dictArray:
            if (len(self.dictArray[elem]) == length and
                self.dictArray[elem] not in output):
                output.append(self.dictArray[elem]) 
        return output
    def rangeDictArray(self) -> Dict:
        ''' словарь dictArray, отфильтрованный по длинам строк '''
        output = {}
        for elem in self.dictArray:
            length = len(self.dictArray[elem])
            if length not in output:
                output[length] = []
            if self.dictArray[elem] not in output[length]:
                output[length].append(self.dictArray[elem])
        return output

s1 = Solution()
s1.lengthOfLongestSubstring("abcabcbb")
# Output: 3
s1.dictArray
# Output: {0: 'abc', 1: 'bca', 2: 'cab', 3: 'abc', 5: 'cb', 7: 'b'}
s1.fetchListsByLength(3)
# Output: ['abc', 'bca', 'cab']
s1.rangeDictArray()
# Output: {3: ['abc', 'bca', 'cab'], 2: ['cb'], 1: ['b']}

s2 = Solution()
s2.lengthOfLongestSubstring("pwwkew")
s2.dictArray
s2.fetchListsByLength(3)
s2.rangeDictArray()

s3 = Solution()
s3.lengthOfLongestSubstring("bbbbb")
# Output: 3
s3.dictArray
# Output: {0: 'b', 1: 'b', 2: 'b', 3: 'b', 4: 'b'}
s3.fetchListsByLength(3)
# Output: []
s3.rangeDictArray()
# Output: {1: ['b']}
