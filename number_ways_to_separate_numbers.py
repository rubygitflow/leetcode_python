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
        if num[0] == '0':
            return 0
        def dfs(back_int, new_pos, new_int, new_len, all_len, tail):
            nonlocal res
            # print("back_int",back_int, 'new_pos',new_pos, "new_int",new_int, "new_len",new_len, "all_len",all_len, "tail",tail,"res",res)
            if tail[0:1] == '0':
                return
            elif (new_pos + new_len) == all_len:
                res += 1
                # print('(new_pos + new_len)  == all_len => res',res)
                return
            elif new_pos > all_len:
                # print('new_pos > all_len')
                return
            elif (new_pos + new_len) > all_len:
                # print('(new_pos + new_len) > all_len')
                return
            elif back_int <= new_int:
                if new_pos + new_len == all_len:
                    res += 1
                    # print('back_int <= new_int  &&  new_pos + new_len == all_len  =>  res',res)
                    return
                else:
                    # print('dfs/1')
                    dfs(new_int, new_pos+new_len, int(tail[new_len:new_len+new_len] or '0'), new_len, all_len, tail[new_len:])
            # print('dfs/2')
            dfs(back_int, new_pos, int(tail[:new_len+1] or '0'), new_len+1, all_len, tail)
            # print('dfs/3')
            dfs(back_int*10+int(tail[:1] or '0'), new_pos+1, int(tail[1:new_len+1+1] or '0'), new_len+1, all_len, tail[1:])

        dfs(int(num[0]), 1, 0, 0, len(num), num[1:])
        # return res
        return res % MOD

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
# Output: 1/14+1/5 == 2
print(Solution().numberOfCombinations("113224345345672356"))
# Output: ? == 10072
print(Solution().numberOfCombinations("1132243453456723562456731925"))
# Output: ? == 1364387
