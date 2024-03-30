# https://leetcode.com/problems/maximum-binary-string-after-change/description/
# 1702. Maximum Binary String After Change

# You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:
# Operation 1: If the number contains the substring "00", you can replace it with "10".
# For example, "00010" -> "10010"
# Operation 2: If the number contains the substring "10", you can replace it with "01".
# For example, "00010" -> "00001"
# Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

# Example 1:
# Input: binary = "000110"
# Output: "111011"
# Explanation: A valid transformation sequence can be:
# "000110" -> "000101" 
# "000101" -> "100101" 
# "100101" -> "110101" 
# "110101" -> "110011" 
# "110011" -> "111011"
# Example 2:
# Input: binary = "01"
# Output: "01"
# Explanation: "01" cannot be transformed any further.

# Constraints:
# 1 <= binary.length <= 105
# binary consist of '0' and '1'.

class Solution(object):
    def maximumBinaryString(self, binary):
        ''' Maximum Binary String After Change '''
        c_first_ones,l = 0,len(binary)
        while c_first_ones<l and binary[c_first_ones]=='1': c_first_ones+=1
        c_zeros = binary.count('0')
        return '1'*c_first_ones+'1'*(c_zeros-1)+'0'*(1 if c_zeros>0 else 0)+'1'*(l-c_first_ones-c_zeros)

print(Solution().maximumBinaryString("000110"))
# Output: "111011"
print(Solution().maximumBinaryString("01"))
# Output: "01"
print(Solution().maximumBinaryString("1101011"))
# Output: "1111011"
