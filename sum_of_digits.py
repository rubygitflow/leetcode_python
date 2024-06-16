# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
# 1945. Sum of Digits of String After Convert

# You are given a string s consisting of lowercase English letters, and an integer k.
# First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
# For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described above.

# Example 1:
# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.

# Example 2:
# Input: s = "leetcode", k = 2
# Output: 6
# Explanation: The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.

# Example 3:
# Input: s = "zbax", k = 2
# Output: 8

# Constraints:
# 1 <= s.length <= 100
# 1 <= k <= 10
# s consists of lowercase English letters.


########################
# https://leetcode.com/problems/happy-number/description/
# 202. Happy Number
# Explanation of the expected solution based on the "Two Pointers" technique:
# https://algo.monster/liteproblems/202

# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

# Constraints:
# 1 <= n <= 231 - 1


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ''' Sum of Digits of String After Convert '''
        offset = ord('a') - 1
        s = ''.join(str(ord(c) - offset) for c in s)
        for _ in range(k):
            t = sum(int(c) for c in s)
            s = str(t)
        return int(s)

    def isHappy(self, n: int) -> bool:
        ''' Happy Number '''
        if n<1: return False

        def iter(num):
            out = 0
            while num:
                num, v = divmod(num, 10)
                out += v * v
            return out

        while not n in [1, 4]:
            n = iter(n)
        return n == 1

print("Sum of Digits of String After Convert")
print(Solution().getLucky("iiii", 1))
# Output: 36
print(Solution().getLucky("leetcode", 2))
# Output: 6
print(Solution().getLucky("zbax", 2))
# Output: 8


print("Happy Number")
print(Solution().isHappy(0))
# Output: false
print(Solution().isHappy(2))
# Output: false
print(Solution().isHappy(2**31 - 1)) # 2147483647
# Output: false
print(Solution().isHappy(4722354576))
# Output: false
print(Solution().isHappy(9999975))
# Output: false

print(Solution().isHappy(7))
# Output: true
print(Solution().isHappy(19))
# Output: true
print(Solution().isHappy(99924))
# Output: true
print(Solution().isHappy(85226))
# Output: true
print(Solution().isHappy(72781))
# Output: true
print(Solution().isHappy(57052))
# Output: true
print(Solution().isHappy(7414))
# Output: true
print(Solution().isHappy(9999976))
# Output: true
