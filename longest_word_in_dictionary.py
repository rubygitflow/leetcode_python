# https://leetcode.com/problems/longest-word-in-dictionary/description/
# 720. Longest Word in Dictionary

# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
# Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

# Example 1:
# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

# Example 2:
# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.

from collections import defaultdict
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        ''' Longest Word in Dictionary '''
        letters_dic = defaultdict(set)
        for i, v in enumerate(words):
            letters_dic[v[0]].add(v)
        max_len, out_word = 0, ''
        for letter in letters_dic:
            set_wrd = letters_dic[letter]
            for w in set_wrd:
                n = len(w)
                # New word can be built one character at a time by the set of words - set_wrd
                if all(w[:i] in set_wrd for i in range(1, n)):
                    if max_len < n:
                        max_len, out_word = n, w
                    elif max_len == n and w < out_word:
                        # lexicographically smaller
                        out_word = w
        return out_word

words = ["w","wo","wor","worl","world"]
# Output: "world"
words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
Solution().longestWord(words)
