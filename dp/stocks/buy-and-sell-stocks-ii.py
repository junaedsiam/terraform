"""
Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
---------

Problem Description:
---------
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

"""


from typing import List


def max_profit_recurse(prices: List[int]) -> int:
    # Time complexity: O(2 ^ n)
    # Space complexity: O(1)
    def solve(i, buy_allowed, prices):
        if i == len(prices):
            # we exhaust the prices list
            return 0
        if buy_allowed:
            # If you buy that means negative balance
            buy = -prices[i] + solve(i + 1, 0, prices)
            not_buy = solve(i + 1, 1, prices)
            return max(buy, not_buy)
        else:
            # if you sell that means positive balance
            sell = prices[i] + solve(i + 1, 1, prices)
            not_sell = solve(i + 1, 0, prices)
            return max(sell, not_sell)

    return solve(0, 1, prices)


def max_profit_memo(prices: List[int]) -> int:
    # Time complexity: O(2n)
    # Space complexity: O(2n) + O(n)
    def solve(i, can_buy, prices, dp):
        if i == len(prices):
            # we exhaust the prices list
            return 0
        if dp[i][can_buy] != -1:
            return dp[i][can_buy]
        take, not_take = None, None

        if can_buy:
            # If you buy that means negative balance
            take = -prices[i] + solve(i + 1, 0, prices, dp)
            not_take = solve(i + 1, 1, prices, dp)
        else:
            # if you sell that means positive balance
            take = prices[i] + solve(i + 1, 1, prices, dp)
            not_take = solve(i + 1, 0, prices, dp)

        dp[i][can_buy] = max(take, not_take)
        return dp[i][can_buy]
    # 2 state for any price. 1. buy 2. not buy
    dp = [[-1] * 2 for _ in range(len(prices))]
    return solve(0, 1, prices, dp)


def max_profit_tabulation(prices):
    # Time complexity: O(2n)
    # Space complexity: O(2n)
    n = len(prices)
    # 2 state for any price. 1. buy 2. not buy
    dp = [[0] * 2 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(0, 2):
            take, not_take = None, None
            if j:
                take = - prices[i] + dp[i + 1][0]
                not_take = dp[i + 1][1]
            else:
                take = prices[i] + dp[i + 1][1]
                not_take = dp[i + 1][0]

            dp[i][j] = max(take, not_take)

    return dp[0][1]


if __name__ == '__main__':
    print(max_profit_tabulation([7, 1, 5, 3, 6, 4]))
