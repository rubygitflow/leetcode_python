# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/
# 2309. Greatest English Letter in Upper and Lower Case

# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
# An English letter b is greater than another letter a if b appears after a in the English alphabet.

# Example 1:
# Input: s = "lEeTcOdE"
# Output: "E"
# Explanation:
# The letter 'E' is the only letter to appear in both lower and upper case.

# Example 2:
# Input: s = "arRAzFif"
# Output: "R"
# Explanation:
# The letter 'R' is the greatest letter to appear in both lower and upper case.
# Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

# Example 3:
# Input: s = "AbCdEfGhIjK"
# Output: ""
# Explanation:
# There is no letter that appears in both lower and upper case.

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase and uppercase English letters.

from collections import defaultdict

class Solution:
    def greatestLetter(self, s: str) -> str:
        ''' Greatest English Letter in Upper and Lower Case '''
        col = defaultdict(int)
        mem = set()
        ans=""
        for c in s:
            if not c in mem:
                mem.add(c)
                upper = c.upper()
                # we have caught a changed character case if the character already exists
                col[upper] += 1
                # processing an additional condition
                ans = (upper if upper > ans else ans) if col[upper] == 2  else ans
        return ans

print(Solution().greatestLetter("l Ee TcOd E "))
# Output: "E"
print(Solution().greatestLetter("a rR AzFif"))
# Output: "R"
print(Solution().greatestLetter("a rr AzFifA"))
# Output: "F"
print(Solution().greatestLetter("AbCdEfGhIjK"))
# Output: ""
print(Solution().greatestLetter("a рр AzФiфA"))
# Output: "Ф"
