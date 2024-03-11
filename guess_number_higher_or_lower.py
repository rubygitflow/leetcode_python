# https://leetcode.com/problems/guess-number-higher-or-lower/description/
# 374. Guess Number Higher or Lower

# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1

# Constraints:
# 1 <= n <= 231 - 1
# 1 <= pick <= n

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
pick = 6
def guess(num: int) -> int:
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        ''' Guess Number Higher or Lower '''
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            G = guess(mid)
            if G == 0:
                return mid
            elif G == -1:
                high = mid - 1
            else:
                low = mid + 1
        return mid      

n = 10
# Output: 6
Solution().guessNumber(n)
