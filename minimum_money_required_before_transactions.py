# https://leetcode.com/problems/minimum-money-required-before-transactions/description/
# 2412. Minimum Money Required Before Transactions
# Explanation from https://algo.monster/liteproblems/2412

from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        ''' Minimum Money Required Before Transactions '''
        total_negative_cash_flow = sum(max(0, cost - cashback) for cost, cashback in transactions)
        max_additional_money_required = 0
        for cost, cashback in transactions:
            if cost > cashback:
                max_additional_money_required = max(
                    max_additional_money_required,
                    total_negative_cash_flow + cashback
                )
            else:
                max_additional_money_required = max(
                    max_additional_money_required,
                    total_negative_cash_flow + cost
                )
        return max_additional_money_required

print(Solution().minimumMoney([[2,1],[5,0],[4,2]]))
# Output: 10
print(Solution().minimumMoney([[3,0],[0,3]]))
# Output: 3
print(Solution().minimumMoney([[7, 2], [5, 0], [4, 1], [5, 8], [5, 9], [0, 10]]))
# Output: 18
