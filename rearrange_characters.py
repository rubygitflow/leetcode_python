# https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/
# 2287. Rearrange Characters to Make Target String

# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.

# Example 1:
# Input: s = "ilovecodingonleetcode", target = "code"
# Output: 2
# Explanation:
# For the first copy of "code", take the letters at indices 4, 5, 6, and 7.
# For the second copy of "code", take the letters at indices 17, 18, 19, and 20.
# The strings that are formed are "ecod" and "code" which can both be rearranged into "code".
# We can make at most two copies of "code", so we return 2.

# Example 2:
# Input: s = "abcba", target = "abc"
# Output: 1
# Explanation:
# We can make one copy of "abc" by taking the letters at indices 0, 1, and 2.
# We can make at most one copy of "abc", so we return 1.
# Note that while there is an extra 'a' and 'b' at indices 3 and 4, we cannot reuse the letter 'c' at index 2, so we cannot make a second copy of "abc".

# Example 3:
# Input: s = "abbaccaddaeea", target = "aaaaa"
# Output: 1
# Explanation:
# We can make one copy of "aaaaa" by taking the letters at indices 0, 3, 6, 9, and 12.
# We can make at most one copy of "aaaaa", so we return 1.

# Constraints:
# 1 <= s.length <= 100
# 1 <= target.length <= 10
# s and target consist of lowercase English letters.

########################
# https://leetcode.com/problems/sum-of-unique-elements/
# 1748. Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from collections import Counter
from typing import List

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ''' Rearrange Characters to Make Target String '''
        cnt1 = Counter(s)
        cnt2 = Counter(target)
        return min(cnt1[c] // v for c, v in cnt2.items())

    def sumOfUnique(self, nums: List[int]) -> int:
        ''' Sum of Unique Elements '''
        cnt = Counter(nums)
        return sum(k for k, v in cnt.items() if v == 1)

print("Rearrange Characters to Make Target String")
print(Solution().rearrangeCharacters("ilovecodingonleetcode","code"))
# Output: 2
print(Solution().rearrangeCharacters("abcba","abc"))
# Output: 1
print(Solution().rearrangeCharacters("abbaccaddaeea","aaaaa"))
# Output: 1
print(Solution().rearrangeCharacters("abbaccaddaeea","фd"))
# Output: 0

print("Sum of Unique Elements")
print(Solution().sumOfUnique([1,2,3,2]))
# Output: 4
print(Solution().sumOfUnique([1,1,1,1,1]))
# Output: 0
print(Solution().sumOfUnique([1,2,3,4,5]))
# Output: 15
