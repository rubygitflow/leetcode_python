# https://leetcode.com/problems/palindrome-number/description/
# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints:
# -231 <= x <= 231 - 1

# Follow up: Could you solve it without converting the integer to a string?

def isPalindromeNumber(x: int) -> bool:
    if x < 0 or (x and x % 10 == 0):
        return False
    y = 0
    while y < x:
        y = y * 10 + x % 10
        x //= 10
    return x in (y, y // 10)

isPalindromeNumber(123435)
isPalindromeNumber(73537)
isPalindromeNumber(900)
isPalindromeNumber(-123435)
isPalindromeNumber(994499)




