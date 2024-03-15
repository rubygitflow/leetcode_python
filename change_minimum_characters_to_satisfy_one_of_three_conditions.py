# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/description/
# 1737. Change Minimum Characters to Satisfy One of Three Conditions

# You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.
# Your goal is to satisfy one of the following three conditions:
# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.
# Return the minimum number of operations needed to achieve your goal.

# Example 1:
# Input: a = "aba", b = "caa"
# Output: 2
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).

# Example 2:
# Input: a = "dabadd", b = "cda"
# Output: 3
# Explanation: The best way is to make condition 1 true by changing b to "eee".

# Constraints:
# 1 <= a.length, b.length <= 105
# a and b consist only of lowercase letters.

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        lena = len(a)
        cnta = [0] * 26
        lenb = len(b)
        cntb = [0] * 26
        max_a = max_b = 0
        # min_a = min_b = 0
        for c in a:
            max_a = max(ord(c) , max_a)
            # min_a = min(ord(c) , min_a)
            cnta[ord(c) - ord('a')] += 1
        max_a -= ord('a')
        # min_a -= ord('a')
        for c in b:
            max_b = max(ord(c) , max_b)
            # min_b = min(ord(c) , min_b)
            cntb[ord(c) - ord('a')] += 1
        max_b -= ord('a')
        # символы a > b
        def count_a_under_b():
            return sum(cnta[:max_b+1])
        # символы b > a
        def count_b_under_a():
            return sum(cntb[:max_a+1])
        # все символы одинаковые
        def same_letter():
            freq_c = 0
            all_c = 0
            for i in range(max(max_a, max_b) + 1):
                all_c += (cnta[i] + cntb[i])
                freq_c = max(freq_c, cnta[i] + cntb[i])
            return all_c - freq_c
        return min(count_a_under_b(), count_b_under_a(), same_letter())

a = "aba", b = "caa"
# Output: 2
a = "dabadd", b = "cda"
# Output: 3
Solution().minCharacters(a, b)

