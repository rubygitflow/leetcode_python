# https://leetcode.com/problems/is-object-empty/description/
# 2727. Is Object Empty

# Given an object or an array, return if it is empty.
# An empty object contains no key-value pairs.
# An empty array contains no elements.
# You may assume the object or array is the output of JSON.parse.

# Example 1:
# Input: obj = {"x": 5, "y": 42}
# Output: false
# Explanation: The object has 2 key-value pairs so it is not empty.

# Example 2:
# Input: obj = {}
# Output: true
# Explanation: The object doesn't have any key-value pairs so it is empty.

# Example 3:
# Input: obj = [null, false, 0]
# Output: false
# Explanation: The array has 3 elements so it is not empty.

# Constraints:
# obj is a valid JSON object or array
# 2 <= JSON.stringify(obj).length <= 105

# Can you solve it in O(1) time?

def is_empty(obj) -> bool:
    # try:
    #     return len(obj) == 0
    # except:
    #     return False
    return not obj

print(is_empty({"x": 5, "y": 42}))
# Output: False
print(is_empty({}))
# Output: True
print(is_empty([None, False, 0]))
# Output: False
print(is_empty([]))
# Output: true
print(is_empty('wer'))
# Output: False
print(is_empty(''))
# Output: True
print(is_empty(4.9))
# Output: False
print(is_empty(None))
# Output: True
