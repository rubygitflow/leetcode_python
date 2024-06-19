# https://leetcode.com/problems/multiply-strings/description/
# 43. Multiply Strings

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ''' Multiply Strings (Simulating Mathematical Multiplication: digit by digit)'''
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        arr = [0] * (m + n)
        for i in range(m):
            a = int(num1[i])
            for j in range(n):
                b = int(num2[j])
                arr[i + j] += a * b
        for i in range(m + n - 1, 0, -1):
            arr[i] += arr[i-1] % 10
            arr[i-1] //= 10
            if arr[i] > 9:
                arr[i-1] += 1
                arr[i] = arr[i] % 10
        i = 0 if arr[0] else 1
        return "".join(str(x) for x in arr[i:])

print(Solution().multiply("2", "3"))
# Output: "6"
print(Solution().multiply("123", "456"))
# Output: "56088"
print(Solution().multiply("999", "9"))
# Output: "8991"
