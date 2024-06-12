# https://leetcode.com/problems/count-special-integers/description/
# 2376. Count Special Integers
# Explanation: https://algo.monster/liteproblems/2376

# We call a positive integer special if all of its digits are distinct.
# Given a positive integer n, return the number of special integers that belong to the interval [1, n].

# Example 1:
# Input: n = 20
# Output: 19
# Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.

# Example 2:
# Input: n = 5
# Output: 5
# Explanation: All the integers from 1 to 5 are special.

# Example 3:
# Input: n = 135
# Output: 110
# Explanation: There are 110 integers from 1 to 135 that are special.
# Some of the integers that are not special are: 22, 114, and 131.

# Constraints:
# 1 <= n <= 2 * 109


#######################
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
# 357. Count Numbers with Unique Digits
# Explanation: https://algo.monster/liteproblems/357

# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

# Example 1:
# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

# Example 2:
# Input: n = 0
# Output: 1

# Constraints:
# 0 <= n <= 8


#######################
# https://leetcode.com/problems/count-numbers-with-unique-digits-ii/description/
# 3032. Count Numbers With Unique Digits II
# Explanation: https://algo.monster/liteproblems/3032

# Given two positive integers a and b, return the count of numbers having unique digits in the range [a, b] (inclusive).

# Example 1:
# Input: a = 1, b = 20
# Output: 19
# Explanation: All the numbers in the range [1, 20] have unique digits except 11. Hence, the answer is 19.

# Example 2:
# Input: a = 9, b = 19
# Output: 10
# Explanation: All the numbers in the range [9, 19] have unique digits except 11. Hence, the answer is 10.

# Example 3:
# Input: a = 80, b = 120
# Output: 27
# Explanation: There are 41 numbers in the range [80, 120], 27 of which have unique digits.

# Constraints:
# 1 <= a <= b <= 1000


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        ''' Count Special Integers '''

        # Permutation function permutations(m, n)
        # that calculates permutations of m elements taken n at a time.
        # Recursive function to calculate permutations: permutations(m, n) = m! / (m-n)!
        def permutations(m, n):
            if n == 0:
                return 1
            else:
                return permutations(m, n - 1) * (m - n + 1)

        # List to keep track of visited digits
        visited = [False] * 10
      
        # Variable to store the count of special numbers
        answer = 0
      
        # Convert the number into a list of its digits in reverse order
        # so we can process the least significant digit first
        digits = [int(c) for c in str(n)[::-1]]
      
        # Length of the number (number of digits)
        num_length = len(digits)
      
        # Count all special numbers with length less than the length of n
        for i in range(1, num_length):
            answer += 9 * permutations(9, i - 1)

        # Count special numbers with the same length as n        
        for i in range(num_length - 1, -1, -1):
            current_digit = digits[i]
          
            # First digit cannot be 0, others can
            start = 1 if i == num_length - 1 else 0
          
            while start < current_digit:
                if not visited[start]:
                    answer += permutations(10 - (num_length - i), i)
                start += 1
          
            # If the current digit has already been visited, stop the loop
            if visited[current_digit]:
                break
          
            # Mark the digit as visited
            visited[current_digit] = True
          
            # If we're at the last digit and haven't broken the loop,
            # then we need to account for this number itself being a special number
            if i == 0:
                answer += 1

        return answer

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ''' Count Numbers with Unique Digits '''
        if n == 0:
            return 1
        out, cur = 10, 9
        for i in range(n - 1):
            cur *= 9 - i
            out += cur
        return out

    def numberCount(self, a: int, b: int) -> int:
        ''' Count Numbers With Unique Digits II '''
        return self.countSpecialNumbers(b) - (self.countSpecialNumbers(a-1) if a > 1 else 0)

print("Count Special Integers")
print(Solution().countSpecialNumbers(5))
# Output: 5
print(Solution().countSpecialNumbers(20))
# Output: 19
print(Solution().countSpecialNumbers(135))
# Output: 110
print(Solution().countSpecialNumbers(320))
# Output: 251
print(Solution().countSpecialNumbers(2 * 10 ** 9))
# Output: 5974650

print("Count Numbers with Unique Digits")
print(Solution().countNumbersWithUniqueDigits(0))
# Output: 1
print(Solution().countNumbersWithUniqueDigits(1))
# Output: 10
print(Solution().countNumbersWithUniqueDigits(2))
# Output: 91
print(Solution().countNumbersWithUniqueDigits(3))
# Output: 739
print(Solution().countNumbersWithUniqueDigits(4))
# Output: 5275
print(Solution().countNumbersWithUniqueDigits(5))
# Output: 32491
print(Solution().countNumbersWithUniqueDigits(6))
# Output: 168571
print(Solution().countNumbersWithUniqueDigits(7))
# Output: 712891
print(Solution().countNumbersWithUniqueDigits(8))
# Output: 2345851

print("Count Numbers With Unique Digits II")
print(Solution().numberCount(1, 20))
# Output: 19
print(Solution().numberCount(9, 19))
# Output: 10
print(Solution().numberCount(80, 120))
# Output: 27
