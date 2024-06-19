# https://leetcode.com/problems/count-and-say/description/
# 38. Count and Say
# https://en.wikipedia.org/wiki/Run-length_encoding
# Explanation: https://algo.monster/liteproblems/38

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

# Example 2:
# Input: n = 1
# Output: "1"
# Explanation:
# This is the base case.

# Constraints:
# 1 <= n <= 30

# Follow up: Could you solve it iteratively?

class Solution:
    def countAndSay(self, n: int) -> str:
        ''' Count and Say '''
        # Initialize the sequence with the first term.
        sequence = '1'
      
        # Build the sequence up to the n-th term.
        # Start with the second step
        for _ in range(n - 1):
            # Design RLE encoding for the sequence

            # Create a temporary string to hold new term
            temp_sequence = ''
             # Initialize index for the current sequence
            index = 0
         
            # Iterate through the current sequence to build the next sequence
            while index < len(sequence):
                # Initialize a count index
                count_index = index
                # Count the number of same digits
                while count_index < len(sequence) and sequence[count_index] == sequence[index]:
                    count_index += 1
              
                # Append the count and the digit itself to the temp_sequence list
                temp_sequence += str(count_index - index)
                temp_sequence += sequence[index]
              
                # Move to the next different digit
                index = count_index
          
            # replace the sequence with the temp_sequence
            sequence = temp_sequence
      
        # After the loop, sequence variable holds the n-th term of the sequence
        return sequence

print(Solution().countAndSay(4))
# Output: "1211"
print(Solution().countAndSay(1))
# Output: "1"
# print(Solution().countAndSay(10))
# # Output: "13211311123113112211"
