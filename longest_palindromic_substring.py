# https://leetcode.com/problems/longest-palindromic-substring/description/
# 5. Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

import time

def longestPalindrome(s: str) -> str:
    ''' Longest Palindromic Substring (the fastest)'''
    t = time.time()
    length = len(s)
    max_length = 0
    output = ''
    for i in range(1,length):
        l, r = i - 1, i
        while l > -1 and r < length:
            if s[l] == s[r]:
                current =  r - l + 1
                if current > max_length:
                    max_length = current
                    output = s[l:r+1]
                l -= 1
                r += 1
            else:
                break
        # odd Palindrome
        l, r = i - 1, i + 1
        while l > -1 and r < length:
            if s[l] == s[r]:
                current =  r - l + 1
                if current > max_length:
                    max_length = current
                    output = s[l:r+1]
                l -= 1
                r += 1
            else:
                break
    print(time.time()-t)
    return output

s = 'hjlsirulivjjjlsjdjsalkjd'
longestPalindrome(s)
# Output: 'sjdjs'
# 3.790855407714844e-05

s = 'hjllllllsirulivjjjlsjdjsalkjd'
longestPalindrome(s)
# Output: 'llllll'
# 3.910064697265625e-05


#######################
def longestPalindromeII(s: str) -> str:
    ''' Longest Palindromic Substring (the slowest)'''
    t = time.time()
    mlen = 0
    start = end = 0
    n = len(s)
    dp = [ [False] * n for i in range(n) ]
    for j in range(n):
        for i in range(j + 1):
            dp[i][j] = (i == j) or (s[i] == s[j] and j - i == 1) or (s[i] == s[j] and dp[i + 1][j - 1])
            if dp[i][j] is True and j - i + 1 > mlen:
                mlen = j - i + 1
                start = i
                end = j
    print(time.time()-t)
    return s[start: end + 1]

s = 'hjlsirulivjjjlsjdjsalkjd'
longestPalindromeII(s)
# Output: 'sjdjs'
# 0.0001957416534423828

s = 'hjllllllsirulivjjjlsjdjsalkjd'
longestPalindromeII(s)
# Output: 'llllll'
# 0.00018215179443359375


#######################
def longestPalindromeIII(s: str) -> str:
    t = time.time()
    n = len(s)
    f = [[True] * n for _ in range(n)]
    k, mx = 0, 1
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            f[i][j] = False
            if s[i] == s[j]:
                f[i][j] = f[i + 1][j - 1]
                if f[i][j] and mx < j - i + 1:
                    k, mx = i, j - i + 1
    print(time.time()-t)
    return s[k : k + mx]

s = 'hjlsirulivjjjlsjdjsalkjd'
longestPalindromeIII(s)
# Output: 'sjdjs'
# 7.557868957519531e-05

s = 'hjllllllsirulivjjjlsjdjsalkjd'
longestPalindromeIII(s)
# Output: 'llllll'
# 8.106231689453125e-05

