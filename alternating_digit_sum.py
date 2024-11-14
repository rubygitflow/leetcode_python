# https://leetcode.com/problems/alternating-digit-sum/description/
# 2544. Alternating Digit Sum

# You are given a positive integer n. Each digit of n has a sign according to the following rules:
# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

# Example 1:
# Input: n = 521
# Output: 4
# Explanation: (+5) + (-2) + (+1) = 4.

# Example 2:
# Input: n = 111
# Output: 1
# Explanation: (+1) + (-1) + (+1) = 1.

# Example 3:
# Input: n = 886996
# Output: 0
# Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.

# Constraints:
# 1 <= n <= 109


#############################
# https://leetcode.com/problems/add-digits/description/
# 258. Add Digits
# Explanation: https://algo.monster/liteproblems/258

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

# Constraints:
# 0 <= num <= 231 - 1

# Follow up: Could you do it without any loop/recursion in O(1) runtime?


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ''' Alternating Digit Sum '''
        return sum((-1) ** i * int(x) for i, x in enumerate(str(n)))

    def addDigits(self, num: int) -> int:
        ''' Add Digits (digital root - Time complexity: O(1))'''
        if num == 0: return 0

        return (num - 1) % 9 + 1;

if __name__ == "__main__":
    print("Alternating Digit Sum")
    print(Solution().alternateDigitSum(521))
    # Output: 4
    print(Solution().alternateDigitSum(111))
    # Output: 1
    print(Solution().alternateDigitSum(886996))
    # Output: 0
    print(Solution().alternateDigitSum(885996))
    # Output: -1
    print(Solution().alternateDigitSum(886995))
    # Output: 1

    print("Add Digits (digital root - Time complexity: O(1))")
    print(Solution().addDigits(38))
    # Output: 2
    print(Solution().addDigits(0))
    # Output: 0
    print(Solution().addDigits(886995))
    # Output: 9
    print(Solution().addDigits(1))
    # Output: 1
