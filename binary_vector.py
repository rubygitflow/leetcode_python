# https://leetcode.com/problems/max-consecutive-ones/description/
# 485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# find the maximum length of a sequence of Ones in a binary vector
# найти максимальную длину последовательности из единиц в бинарном векторе 

def longOne(binary_list):
    maxLength = 0
    length = 0
    for i in binary_list:
        if i == 1:
            length += 1
            maxLength = max(maxLength, length)
        else:
            length = 0
    return maxLength

longOne([0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1])
# Output: 4 
longOne([0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1])
# Output: 6
longOne([0,0,0,0,])
# Output: 0

###################
# Find all sequences of Ones in a binary vector
# найти все последовательности из единиц в бинарном векторе 
def allOne(binary_list):
    output = {}
    left = 0
    length = 0
    for i, n in enumerate(binary_list):
        if n == 1:
            if length == 0:
                left = i
                output[left] = 1
            else:
                output[left] += 1
            length = output[left]
        else:
            length = 0
    return output

allOne([0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1])
# Output: {3: 2, 6: 1, 8: 1, 10: 4, 15: 1}
allOne([0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1])
# Output: {3: 2, 6: 1, 8: 6, 15: 1}
allOne([0,0,0,0,])
# Output: {}
allOne([1,1,1,1,])
# Output: {0: 4}
