# https://leetcode.com/problems/partition-labels/description/
# 763. Partition Labels

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

# Example 1:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:
# Input: s = "eccbbbbdec"
# Output: [10]

# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.

from typing import List

def partitionLabels(s: str) -> List[int]:
    # составляем словарь последних мест появления символа в строке
    last = {c: i for i, c in enumerate(s)}
    mx = j = 0
    ans = []
    for i, c in enumerate(s):
        # сдвигаем границу интервала
        # пока не дошли до символа с последним появлением в строке
        mx = max(mx, last[c]) 
        # по достижению границы для группы символов
        if mx == i:
            # фиксируем длину отрезка символов
            ans.append(i - j + 1)
            # и назначаем индекс начала следующего списка
            j = i + 1
    return ans

s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Input: s = "eccbbbbdec"
# Output: [10]
partitionLabels(s)
