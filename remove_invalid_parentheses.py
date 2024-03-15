# https://leetcode.com/problems/remove-invalid-parentheses/description/
# 301. Remove Invalid Parentheses

# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()","()()()"]

# Example 2:
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]

# Example 3:
# Input: s = ")("
# Output: [""]

# Constraints:
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.

from typing import List

class Solution:
  def removeInvalidParentheses(self, s: str) -> List[str]:
    def getLeftAndRightCounts(s: str) -> tuple:
      l = 0
      r = 0
      for c in s:
        if c == '(':
          l += 1
        elif c == ')':
          if l == 0:
            r += 1
          else:
            l -= 1
      return l, r
    def isValid(s: str):
      count = 0  # Number of '(' - # Of ')'
      for c in s:
        if c == '(':
          count += 1
        elif c == ')':
          count -= 1
        if count < 0:
          return False
      return True  # Count == 0
    output = []
    def dfs(s: str, start: int, l_couts: int, r_couts: int) -> None:
      if l_couts == 0 and r_couts == 0 and isValid(s):
        output.append(s)
        return
      for i in range(start, len(s)):
        if i > start and s[i] == s[i - 1]:
          continue
        if r_couts > 0 and s[i] == ')':  # Delete s[i]
          dfs(s[:i] + s[i + 1:], i, l_couts, r_couts - 1)
        elif l_couts > 0 and s[i] == '(':  # Delete s[i]
          dfs(s[:i] + s[i + 1:], i, l_couts - 1, r_couts)
    l_couts, r_couts = getLeftAndRightCounts(s)
    dfs(s, 0, l_couts, r_couts)
    return output


s = "()())())"
# Output: ['(()())', '(())()', '()(())', '()()()']

s = "(a)())()"
# Output: ["(a())()","(a)()()"]

s = ")("
# Output: [""]

Solution().removeInvalidParentheses(s)
