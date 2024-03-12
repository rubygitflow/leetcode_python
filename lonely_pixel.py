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

picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
# Output: 3
picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
# Output: 0
Solution().findLonelyPixel(picture)


