# https://leetcode.com/problems/lonely-pixel-i/description/
# 531. Lonely Pixel I

# Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.
# A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

# Example 1:
# Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.

# Example 2:
# Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
# Output: 0

# Constraints:
# m == picture.length
# n == picture[i].length
# 1 <= m, n <= 500
# picture[i][j] is 'W' or 'B'.


#######################
# https://leetcode.com/problems/lonely-pixel-ii/description/
# 533 - Lonely Pixel II

# Given an m x n picture consisting of black 'B' and white 'W' pixels and an integer target, return the number of black lonely pixels.
# A black lonely pixel is a character 'B' that located at a specific position (r, c) where:
# Row r and column c both contain exactly target black pixels.
# For all rows that have a black pixel at column c, they should be exactly the same as row r.

# Example 1:
# Input: picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3
# Output: 6
# Explanation: All the green 'B' are the black pixels we need (all 'B's at column 1 and 3).
# Take 'B' at row r = 0 and column c = 1 as an example:
#  - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black pixels. 
#  - Rule 2, the rows have black pixel at column c = 1 are row 0, row 1 and row 2. They are exactly the same as row r = 0.

# Example 2:
# Input: picture = [["W","W","B"],["W","W","B"],["W","W","B"]], target = 1
# Output: 0

# Constraints:
# m == picture.length
# n == picture[i].length
# 1 <= m, n <= 200
# picture[i][j] is 'W' or 'B'.
# 1 <= target <= min(m, n)

from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        ''' Lonely Pixel I '''
        count = 0
        for i, v in enumerate(picture):
            for j, w in enumerate(v):
                if w=='B':
                    if( (i > 0 and picture[i-1] == "B") or
                        (j > 0 and v[j-1] == "B" ) or
                        (i < len(picture) - 1 and picture[i+1] == "B") or
                        (j < len(v) - 1 and v[j+1] == "B") ):
                        continue
                    else:
                        count += 1
        return count 
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        ''' Lonely Pixel II (???) '''
        m, n = len(picture), len(picture[0])
        rows = [0] * m
        cols = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j].append(i)
        t = [[False] * m for _ in range(m)]
        for i in range(m):
            for k in range(i, m):
                if i == k:
                    t[i][k] = True
                else:
                    t[i][k] = all([picture[i][j] == picture[k][j] for j in range(n)])
                t[k][i] = t[i][k]
        res = 0
        for i in range(m):
            if rows[i] == target:
                for j in range(n):
                    if len(cols[j]) == target and all([t[i][k] for k in cols[j]]):
                        res += 1
        return res

picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
# Output: 3
picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
# Output: 0
Solution().findLonelyPixel(picture)

picture, target = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], 3
# Output: 6
picture, target = [["W","W","B"],["W","W","B"],["W","W","B"]], 1
# Output: 0
picture, target = [["W","W","B"],["W","W","W"],["W","W","W"]], 1
# Output: 1
Solution().findBlackPixel(picture, target)

