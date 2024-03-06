# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

#######################
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# 122. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

#######################
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# 123. Best Time to Buy and Sell Stock III

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 105

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' Best Time to Buy and Sell Stock '''
        if not prices:
            return 0
        l, r = 0, 1
        max_price = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_price = max(max_price, profit)
            else:
                l = r
            r += 1
        return max_price
    def maxProfitII(self, prices: List[int]) -> int:
        ''' Best Time to Buy and Sell Stock II '''
        return sum( [prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1]] )
    def maxProfitIII(self, prices: List[int]) -> int:
        ''' Best Time to Buy and Sell Stock III '''
        deals = [[prices[i - 1], prices[i]] for i in range(1, len(prices)) if prices[i] > prices[i - 1]]
        if not deals: return 0
        merged_deals = [deals[0]]
        for i in range(1, len(deals)):
            if deals[i][0] == merged_deals[-1][1]:
                merged_deals[-1][1] = deals[i][1]
            else:
                merged_deals.append(deals[i])
        profits = [deal[1] - deal[0] for deal in merged_deals]
        return sum(sorted(profits)[-2:])

prices = [7,1,5,3,6,4]
# Output: 5
prices = [7,6,4,3,1]
# Output: 0
Solution().maxProfit(prices)

prices = [7,1,5,3,6,4]
# Output: 7
prices = [1,2,3,4,5]
# Output: 4
Solution().maxProfitII(prices)

prices = [3,3,5,0,0,3,1,4]
# Output: 6
Solution().maxProfitIII(prices)
