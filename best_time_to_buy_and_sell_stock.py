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

#######################
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
# 714. Best Time to Buy and Sell Stock with Transaction Fee

# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.

# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# Example 2:
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

# Constraints:
# 1 <= prices.length <= 5 * 104
# 1 <= prices[i] < 5 * 104
# 0 <= fee < 5 * 104

#######################
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# 309. Best Time to Buy and Sell Stock with Cooldown

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0

# Constraints:
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000

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
    def __makeDeals(self, prices: List[int]) -> List[int]:
        deals = [[prices[i - 1], prices[i]] for i in range(1, len(prices)) if prices[i] > prices[i - 1]]
        if not deals: return []
        merged_deals = [deals[0]]
        for i in range(1, len(deals)):
            if deals[i][0] == merged_deals[-1][1]:
                merged_deals[-1][1] = deals[i][1]
            else:
                merged_deals.append(deals[i])
        return merged_deals
    def maxProfitIII(self, prices: List[int]) -> int:
        ''' Best Time to Buy and Sell Stock III '''
        deals = self.__makeDeals(prices)
        profits = [deal[1] - deal[0] for deal in deals]
        return sum(sorted(profits)[-2:])
    def maxProfitAfterFee(self, prices: List[int], fee: int) -> int:
        ''' Best Time to Buy and Sell Stock with Transaction Fee '''
        deals = self.__makeDeals(prices)
        # We can squeeze profit from combining intervals with small overlaps,
        # smaller than the fee size
        merged_deals = [deals[0]]
        for i in range(1, len(deals)):
            if(merged_deals[-1][0] < deals[i][0] and
               merged_deals[-1][1] < deals[i][0] + fee):
                merged_deals[-1][1] = deals[i][1]
            else:
                merged_deals.append(deals[i])
        return sum(
            [deal[1] - deal[0] - fee for deal in merged_deals if (deal[1] - deal[0] - fee) > 0]
        )
    def maxProfitWithHold(self, prices: List[int]) -> int:
        ''' Best Time to Buy and Sell Stock with Cooldown '''
        sold = 0                # Represents the maximum profit if the stock is sold on the current day
        hold = float('-inf')    # Represents the maximum profit if the stock is held (bought) on the current day
        rest = 0                # Represents the maximum profit if no action is taken (rest) on the current day
        for price in prices:    # Iterating through each day's stock price
            prev_sold = sold    # Storing the previous value of 'sold' for updating 'rest'
            # Updating 'sold' with the profit from holding the stock on the previous day plus the current day's stock price
            sold = hold + price
            # Updating 'hold' to the maximum of its current value and the profit from resting on the previous day minus the current day's stock price
            hold = max(hold, rest - price)
            # Updating 'rest' to the maximum of its current value and the profit from selling the stock on the previous day
            rest = max(rest, prev_sold)
        # Returning the maximum profit achievable, which is the maximum between 'sold' and 'rest'
        return max(sold, rest)

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

prices, fee = [1,3,2,8,4,9], 2
# Output: 8
prices, fee = [1,3,7,5,10,3], 3
# Output: 6
prices, fee = [8,9,7,6,8,8], 2
# Output: 0
Solution().maxProfitAfterFee(prices, fee)

prices = [1,2,3,0,2]
# Output: 3
Solution().maxProfitWithHold(prices)
