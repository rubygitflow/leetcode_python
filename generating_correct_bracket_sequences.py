# https://leetcode.com/problems/generate-parentheses/description/
# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

# Generating correct bracket sequences
# https://habr.com/ru/companies/yandex/articles/449890/#:~:text=%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0%20D.%20%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B9

# Правильные скобочные последовательности
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D1%81%D0%BA%D0%BE%D0%B1%D0%BE%D1%87%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8

# n = [1..15]
# Для заданных n пар скобок напишите функцию для подсчета всех комбинаций правильно сформированных скобок.

from typing import List
import math

class Solution:
    def generateParenthesis(self, nCouples: int) -> List[str]:
        ''' Generate Parentheses '''
        def dfs(accum, l, r):
            if l == nCouples == r:
                res_arr.append(accum)
                return
            if l < nCouples:
                dfs(accum + '(', l + 1, r)
            if r < l:
                dfs(accum + ')', l, r + 1)

        res_arr = []
        dfs('(', 1, 0)
        return res_arr

    def calculateParenthesisPermutation(self, nCouples: int) -> int:
        ''' Calculate Parentheses Permutation'''
        def dfs(l, r):
            nonlocal res_count
            if l == nCouples == r:
                res_count += 1
                return
            if l < nCouples:
                dfs(l + 1, r)
            if r < l:
                dfs(l, r + 1)

        res_count = 0 # -1 sec for nCouples=15 
        dfs(1, 0)
        return res_count

    def countWellFormedParenthesis(self, nCouples: int) -> int:
        ''' Count Well Formed Parenthesis By The Formula'''
        return math.comb(2 * nCouples, nCouples) // (nCouples+1)

if __name__ == "__main__":
    print(Solution().generateParenthesis(2))
    # Output: ["(())", "()()"]
    print(Solution().calculateParenthesisPermutation(2))
    # Output: 2
    print(Solution().countWellFormedParenthesis(15))
    # Output: 9694845
    # import time
    # t = time.time()
    # res = Solution().calculateParenthesisPermutation(15)
    # print(time.time()-t, res)
    print(Solution().calculateParenthesisPermutation(15))
    # Output: 9694845
