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

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        ''' Count Special Integers '''

        # Recursive function to calculate permutations A(m, n) = m! / (m-n)!
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
