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
        dfs(int(num[0:1] or '0'), 1, 1, len(num), num[1:])
        return res + 1

    # https://leetcode.com/problems/number-of-ways-to-separate-numbers/solutions/1424057/python3-dp/
    # Explanation: https://www.youtube.com/watch?v=xe6mfpv1JFA
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
    def numberOfCombinationsVerifyEx(self, num: str) -> int:
        # Helper function to compare the lexicographical order of two numbers within 'num'
        # representing the start indices and their length 'length'.
        def is_greater_or_equal(start1, start2, length):
            common_prefix_length = longest_common_prefix[start1][start2]
            return common_prefix_length >= length or num[start1 + common_prefix_length] >= num[start2 + common_prefix_length]

        num_length = len(num)

        # Pre-compute the longest common prefix (LCP) array.
        longest_common_prefix = [[0] * (num_length + 1) for _ in range(num_length + 1)]
        for i in range(num_length - 1, -1, -1):
            for j in range(num_length - 1, -1, -1):
                if num[i] == num[j]:
                    longest_common_prefix[i][j] = 1 + longest_common_prefix[i + 1][j + 1]
        # print("longest_common_prefix",longest_common_prefix)

        # Dynamic programming table where dp[i][j] represents the number of combinations
        # of valid integers with length 'j' that end at index 'i - 1'.
        dp = [[0] * (num_length + 1) for _ in range(num_length + 1)]
        dp[0][0] = 1

        # Build up the DP table.
        for i in range(1, num_length + 1):
            for j in range(1, i + 1):
                current_value = 0
                if num[i - j] != '0':  # Skip numbers with leading zero.
                    if i - j - j >= 0 and is_greater_or_equal(i - j, i - j - j, j):
                        # The substring is greater or equal to the previous,
                        # so we can safely append to the previous.
                        current_value = dp[i - j][j]
                    else:
                        # Take the combination counts from the smaller number if present.
                        current_value = dp[i - j][min(j - 1, i - j)]

                # Update the current dp value including the current value with MOD.
                # Accumulate with the previous j-1 combinations.
                dp[i][j] = (dp[i][j - 1] + current_value) % MOD

        # Total number of combinations is the last value in the dp table.
        return dp[num_length][num_length]


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
print(Solution().numberOfCombinations("1122")) # solution building test
# Output: 1/1111+1/22+1/112+1/13+1/4 == 5
print(Solution().numberOfCombinations("11022"))
# Output: 1/14+1/122+1/5 == 3
print(Solution().numberOfCombinations("113224345345672356"))
# Output: ? == 180
print(Solution().numberOfCombinations("1132243453456723562456731925"))
# Output: ? == 1215
# print(Solution().numberOfCombinations("113224345345672356245673192511322434534567235624567319251132243453456723562456731925242435"))
# # Output: ? == 2685486 # 90 digits - 3 seconds
# print(Solution().numberOfCombinations("113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583"))
# # Output: ? == 156786812 # it does not cope in 60 minutes :(

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
print(Solution().numberOfCombinationsVerify("113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583"))
# Output: ? == 156786812  # counts in a second

print("Number of Ways to Separate Numbers (VerifyEx)")
print(Solution().numberOfCombinationsVerifyEx("327"))
# Output: 2
print(Solution().numberOfCombinationsVerifyEx("094"))
# Output: 0
print(Solution().numberOfCombinationsVerifyEx("0"))
# Output: 0
print(Solution().numberOfCombinationsVerifyEx("1122"))
# Output: 1/1111+1/22+1/112+1/13+1/4 == 5
print(Solution().numberOfCombinationsVerifyEx("11022"))
# Output: 1/14+1/122+1/5 == 3
print(Solution().numberOfCombinationsVerifyEx("113224345345672356"))
# Output: ? == 180
print(Solution().numberOfCombinationsVerifyEx("1132243453456723562456731925"))
# Output: ? == 1215
print(Solution().numberOfCombinationsVerifyEx("113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583113224345345672356245673192583"))
# Output: ? == 156786812  # counts in a second
