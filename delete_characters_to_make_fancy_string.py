# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
# 1957. Delete Characters to Make Fancy String

# A fancy string is a string where no three consecutive characters are equal.
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
# Return the final string after the deletion. It can be shown that the answer will always be unique.

# Example 1:
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".
# Example 2:

# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".

# Example 3:
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".

# Constraints:
# 1 <= s.length <= 105
# s consists only of lowercase English letters.

from functools import reduce

class Solution:
    def makeFancyString(self, s: str) -> str:
        ''' Delete Characters to Make Fancy String '''
        output = ''
        for c in s:
            if len(output) > 1 and output[-1] == output[-2] == c:
                continue
            output += c
        return output

    def makeFancyStringII(self, s: str) -> str:
        ''' Delete Characters to Make Fancy String (reduce)'''
        return reduce(lambda acc, ch: (acc[0] if ch == acc[1] and ch == acc[2] else acc[0] + ch, ch, acc[1]), list(s), ('','',''))[0]

s = "leeetcode"
print(Solution().makeFancyString(s))
# Output: "leetcode"
s = "aaabaaaa"
print(Solution().makeFancyString(s))
# Output: "aabaa"
print(Solution().makeFancyString("aab"))
# Output: "aab"

s = "leeetcode"
print(Solution().makeFancyStringII(s))
# Output: "leetcode"
s = "aaabaaaa"
print(Solution().makeFancyStringII(s))
# Output: "aabaa"
print(Solution().makeFancyStringII("aab"))
# Output: "aab"
