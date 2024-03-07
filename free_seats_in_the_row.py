# Free seats in the row
# Свободные места в ряду
# Определить, на каком максимальном расстоянии от посетителей можно сесть в ряду.
# [1,0,0,1]
# # Output: 1
# [1,0,0,1,0,0,0,0,1]
# # Output: 2
# [1,1,0,1,1,0,0,0,1]
# # Output: 2
# [1,1,0,1,1,0,0,0,0]
# # Output: 4

from typing import List

class Solution:
    def takeFreeSeat(self, row: List[int]) -> int:
        if not row:
            return 0
        l, max_dist = 0, 0
        for r, p in enumerate(row):
            if p == 0:
                if row[l] != row[r]:
                    l = r
                if r == len(row) - 1:
                   max_dist = max(max_dist, r - l + 1)
            else:
                if r == l:
                    continue 
                if row[l] != row[r]:
                    if l == 0:
                        max_dist = r - l
                    else:
                        total = r - l
                        if total % 2 == 0:
                            max_dist = max(max_dist, total // 2)
                        else:
                            max_dist = max(max_dist, total // 2 + 1)
                    l = r
        return max_dist

r = [1,0,0,1]
# Output: 1
r = [1,0,0,1,0,0,0,0,1]
# Output: 2
r = [1,1,0,1,1,0,0,0,1]
# Output: 2
r = [1,1,0,1,1,0,0,0,0]
# Output: 4
r = [0,0,0,0]
# Output: 4
r = [0,0,0,1]
# Output: 3
Solution().takeFreeSeat(r)
