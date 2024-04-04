# https://leetcode.com/problems/maximum-number-of-balloons/
# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ''' Maximum Number of "Balloon"s '''
        b  = text.count('b')
        a  = text.count('a')
        l  = text.count('l')//2
        o  = text.count('o')//2
        n  = text.count('n')
        return min(b,a,l,o,n)
    def maxNumberOfBalloonsEx(self, text: str) -> int:
        ''' Maximum Number of "Balloon"s '''
        cnt = Counter(text)
        cnt['o'] >>= 1
        cnt['l'] >>= 1
        return min(cnt[c] for c in 'balon')

print(Solution().maxNumberOfBalloons("nlaebolko"))
# Output: 1
print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
# Output: 2
print(Solution().maxNumberOfBalloons("leetcode"))
# Output: 0
print(Solution().maxNumberOfBalloons("regret"))
# Output: 0

print(Solution().maxNumberOfBalloonsEx("nlaebolko"))
# Output: 1
print(Solution().maxNumberOfBalloonsEx("loonbalxballpoon"))
# Output: 2
print(Solution().maxNumberOfBalloonsEx("leetcode"))
# Output: 0
print(Solution().maxNumberOfBalloonsEx("regret"))
# Output: 0
