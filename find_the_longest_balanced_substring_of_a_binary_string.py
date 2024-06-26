# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/
# 2609. Find the Longest Balanced Substring of a Binary String

# You are given a binary string s consisting only of zeroes and ones.
# A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.
# Return the length of the longest balanced substring of s.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.

# Example 2:
# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4. 

# Example 3:
# Input: s = "111"
# Output: 0
# Explanation: There is no balanced substring except the empty substring, so the answer is 0.

# Constraints:
# 1 <= s.length <= 50
# '0' <= s[i] <= '1'

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(0,len(s)-1):
            if (s[i] == '0' and s[i+1] == '1') or s[i] == '1' and s[i+1] == '0':
                k = 1
                max_len = max(max_len, k*2)
                while ((i-k) > -1 or (i+1) < len(s)) and s[i] == s[i-k] and s[i+1] == s[i+1+k]:
                    k += 1
                    max_len = max(max_len, k*2)
        return max_len
    def findTheLongestBalancedSubstringII(self, s: str) -> int:
        out = 0
        zeros = 0
        ones = 0
        for letter in s:
            if letter=="0":
                if ones==0:
                    # continue counting
                    zeros += 1
                else:
                    # break counting
                    ones = 0
                    zeros = 1
            elif letter=="1":
                if zeros>0:
                    ones += 1
                    # compare ones with zeros and add to result
                    out = min(zeros, ones)
        # fix the result
        return out * 2


print('findTheLongestBalancedSubstring')
s = "01000111"
print(Solution().findTheLongestBalancedSubstring(s))
# Output: 6
s = "00111"
print(Solution().findTheLongestBalancedSubstring(s))
# Output: 4
s = "111"
print(Solution().findTheLongestBalancedSubstring(s))
# Output: 0
s = "111011"
print(Solution().findTheLongestBalancedSubstring(s))
# Output: 2

print('findTheLongestBalancedSubstringII')
s = "01000111"
print(Solution().findTheLongestBalancedSubstringII(s))
# Output: 6
s = "00111"
print(Solution().findTheLongestBalancedSubstringII(s))
# Output: 4
s = "111"
print(Solution().findTheLongestBalancedSubstringII(s))
# Output: 0
s = "111011"
print(Solution().findTheLongestBalancedSubstringII(s))
# Output: 2
