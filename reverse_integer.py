# https://leetcode.com/problems/reverse-integer/description/
# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1

def reverse(x: int):
    output = 0
    mi, mx = -(2**31), 2**31 - 1
    while x:
        if output < mi // 10 + 1 or output > mx // 10:
            return 0
        y = x % 10
        if x < 0 and y > 0:
            y -= 10
        output = output * 10 + y
        x = (x - y) // 10
    return output

reverse(1647380)
# Output: 837461
