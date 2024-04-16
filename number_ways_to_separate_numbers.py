# https://leetcode.com/problems/number-of-ways-to-separate-numbers/description/
# 1977. Number of Ways to Separate Numbers

# You wrote down many positive integers in a string called num. However, you realized that you forgot to add commas to seperate the different numbers. You remember that the list of integers was non-decreasing and that no integer had leading zeros.
# Return the number of possible lists of integers that you could have written down to get the string num. Since the answer may be large, return it modulo 109 + 7.

# Example 1:
# Input: num = "327"
# Output: 2
# Explanation: You could have written down the numbers:
# 3, 27
# 327

# Example 2:
# Input: num = "094"
# Output: 0
# Explanation: No numbers can have leading zeros and all numbers must be positive.

# Example 3:
# Input: num = "0"
# Output: 0
# Explanation: No numbers can have leading zeros and all numbers must be positive.

# Constraints:
# 1 <= num.length <= 3500
# num consists of digits '0' through '9'.

MOD = 10**9 + 7

class Solution:
    def numberOfCombinationsEx(self, num: str) -> int:
        ''' Number of Ways to Separate Numbers (with a non-increasing series of numbers) '''
        res = 0
        if num[0] == '0':
            return 0

        back_char = int(num[0])
        for i in range(1,len(num)):
            char = int(num[i])
            if char > back_char:
                res += 1
            back_char = char
        return (res + 1) % MOD

    def numberOfCombinations(self, num: str) -> int:
        ''' Number of Ways to Separate Numbers (with a non-decreasing integers) '''
        res = 0
        if num[0:1] == '0':
            return 0

        def dfs(back_int, new_pos, step, all_len, tail):
            nonlocal res
            # print('back_int',back_int, 'new_pos',new_pos, 'step',step, 'all_len', all_len,'tail',tail)
            if tail[0:1] == '0':
                right = 0
            else:
                right = int(tail or 0)
            if back_int <= right:
                res += 1
                # print(res,back_int,right)

            if new_pos == all_len:
                return
            if new_pos + step > all_len:
                return

            new_int_s = tail[0:step]
            if new_int_s[0:1] == '0':
                # print('>>')
                dfs(back_int*10+int(new_int_s[0]), new_pos + 1, step+1, all_len, tail[1:])
            else:
                new_int = int(new_int_s or '0')
                if back_int <= new_int:
                    # print('>>>')
                    dfs(new_int, new_pos+step, step, all_len, tail[step:])
                else:
                    next_step = step+1
                    new_int_s = tail[0:next_step]
                    new_int = int(new_int_s or '0')
                    # print('>>>>')
                    dfs(new_int, new_pos+next_step, next_step, all_len, tail[next_step:])
                # print('>>>>>')
                dfs(back_int*10 + int(tail[0:1] or '0'), new_pos + 1, step + 1, all_len, tail[1:])

        # print('>')
        dfs(int(num[0:1] or '-1'), 1, 1, len(num), num[1:])
        return res + 1

    # https://leetcode.com/problems/number-of-ways-to-separate-numbers/solutions/1424057/python3-dp/
    def numberOfCombinationsVerify(self, num: str) -> int:
        ''' Number of Ways to Separate Numbers (for Verification) '''
        n = len(num)
        lcs = [[0]*(n+1) for _ in range(n)]
        for i in reversed(range(n)):
            for j in reversed(range(i+1, n)):
                if num[i] == num[j]: lcs[i][j] = 1 + lcs[i+1][j+1]

        def cmp(i, j, d):
            """Return True if """
            m = lcs[i][j]
            if m >= d: return True
            return num[i+m] <= num[j+m]

        dp = [[0]*(n+1) for _ in range(n)]
        for i in range(n):
            if num[i] != "0":
                for j in range(i+1, n+1):
                    if i == 0: dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j-1]
                        if 2*i-j >= 0 and cmp(2*i-j, i, j-i): dp[i][j] += dp[2*i-j][i]
                        if 2*i-j+1 >= 0 and not cmp(2*i-j+1, i, j-i-1): dp[i][j] += dp[2*i-j+1][i]
        return sum(dp[i][n] for i in range(n)) % MOD



print("Number of Ways to Separate Numbers (with a non-increasing series of numbers)")
print(Solution().numberOfCombinationsEx("327"))
# Output: 2
print(Solution().numberOfCombinationsEx("094"))
# Output: 0
print(Solution().numberOfCombinationsEx("0"))
# Output: 0

print("Number of Ways to Separate Numbers (with a non-decreasing integers)")
print(Solution().numberOfCombinations("327"))
# Output: 2
print(Solution().numberOfCombinations("094"))
# Output: 0
print(Solution().numberOfCombinations("0"))
# Output: 0
print(Solution().numberOfCombinations("1122"))
# Output: 1/1111+1/22+1/112+1/13+1/4 == 5
print(Solution().numberOfCombinations("11022"))
# Output: 1/14+1/122+1/5 == 3
print(Solution().numberOfCombinations("113224345345672356"))
# Output: ? == 180
print(Solution().numberOfCombinations("1132243453456723562456731925"))
# Output: ? == 1215

print("Number of Ways to Separate Numbers (Verify)")
print(Solution().numberOfCombinationsVerify("327"))
# Output: 2
print(Solution().numberOfCombinationsVerify("094"))
# Output: 0
print(Solution().numberOfCombinationsVerify("0"))
# Output: 0
print(Solution().numberOfCombinationsVerify("1122"))
# Output: 1/1111+1/22+1/112+1/13+1/4 == 5
print(Solution().numberOfCombinationsVerify("11022"))
# Output: 1/14+1/122+1/5 == 3
print(Solution().numberOfCombinationsVerify("113224345345672356"))
# Output: ? == 180
print(Solution().numberOfCombinationsVerify("1132243453456723562456731925"))
# Output: ? == 1215
