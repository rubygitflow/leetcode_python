# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ''' Minimum Bit Flips to Convert Number '''
        return bin(start ^ goal).count('1')

    def minBitFlipsII(self, start: int, goal: int) -> int:
        ''' Minimum Bit Flips to Convert Number II'''
        tmp = start ^ goal
        out = 0
        while tmp:
            out += tmp & 1
            tmp >>= 1
        return out

print(Solution().minBitFlips(10, 7))
# Output: 3
print(Solution().minBitFlips(3, 4))
# Output: 3
print(Solution().minBitFlips(10**9, 1))
# Output: 14

print(Solution().minBitFlipsII(10, 7))
# Output: 3
print(Solution().minBitFlipsII(3, 4))
# Output: 3
print(Solution().minBitFlipsII(10**9, 1))
# Output: 14
