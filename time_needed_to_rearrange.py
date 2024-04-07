# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/description/
# 2380. Time Needed to Rearrange a Binary String

# You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.
# Return the number of seconds needed to complete this process.

# Example 1:
# Input: s = "0110101"
# Output: 4
# Explanation: 
# After one second, s becomes "1011010".
# After another second, s becomes "1101100".
# After the third second, s becomes "1110100".
# After the fourth second, s becomes "1111000".
# No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
# so we return 4.

# Example 2:
# Input: s = "11100"
# Output: 0
# Explanation:
# No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
# so we return 0.

# Constraints:
# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.

class Solution:
    def secondsToRemoveOccurrencesBF(self, s: str) -> int:
        ''' Time Needed to Rearrange a Binary String (BRUTE FORCE)'''
        output = 0
        while s.count('01'):
            s = s.replace('01', '10')
            output += 1
        return output

    def secondsToRemoveOccurrences(self, s: str) -> int:
        ''' Time Needed to Rearrange a Binary String (AN UNOBVIOUS SOLUTION)'''
        output = zeroes = 0
        for c in s:
            if c == "1":
                if zeroes:
                    output = max(output+1,zeroes)
            else:
                zeroes+=1
        return output
                
    def secondsToRemoveOccurrencesSingleThreaded(self, s: str) -> int:
        ''' Time Needed to Rearrange a Binary String (ALL PERMUTATIONS)'''
        output = possible = 0
        for c in s:
            if c == '1':
                if possible:
                    output += possible
            else:
                possible += 1
        return output

print(Solution().secondsToRemoveOccurrencesBF("0110001"))
# Output: 4
print(Solution().secondsToRemoveOccurrencesBF("0110101"))
# Output: 4
print(Solution().secondsToRemoveOccurrencesBF("11100"))
# Output: 0

print(Solution().secondsToRemoveOccurrences("0110001"))
# Output: 4
print(Solution().secondsToRemoveOccurrences("0110101"))
# Output: 4
print(Solution().secondsToRemoveOccurrences("11100"))
# Output: 0

print(Solution().secondsToRemoveOccurrencesSingleThreaded("0110001"))
# Output: 6
print(Solution().secondsToRemoveOccurrencesSingleThreaded("0110101"))
# Output: 7
print(Solution().secondsToRemoveOccurrencesSingleThreaded("11100"))
# Output: 0
