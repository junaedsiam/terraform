"""
Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
---------

Problem Description:
---------

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0

"""


def max_profit_memo(prices):
    # Time Complexity: O(2n)
    # Space Complexity: O(2n) + n
    def solve(i, can_buy, prices, dp):
        if i >= len(prices):
            return 0

        if dp[i][can_buy] != -1:
            return dp[i][can_buy]

        if can_buy:
            dp[i][can_buy] = max(-prices[i] + solve(i + 1, 0, prices, dp),
                                 solve(i + 1, 1, prices, dp))
        else:
            # After selling we will jump i + 2 instead i + 1 as
            # we are not allowed to buy after the sell day
            dp[i][can_buy] = max(prices[i] + solve(i + 2, 1, prices, dp),
                                 solve(i + 1, 0, prices, dp))

        return dp[i][can_buy]

    dp = [[-1] * 2 for _ in range(len(prices))]
    return solve(0, 1, prices, dp)


def max_profit_tabulation(prices):
    # Time Complexity: O(2n)
    # Space Complexity: O(2n)
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 2)]

    for i in range(n - 1, -1, -1):
        for j in range(2):
            if j:
                dp[i][j] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            else:
                dp[i][j] = max(prices[i] + dp[i + 2][1], dp[i + 1][0])

    return dp[0][1]


if __name__ == '__main__':
    print(max_profit_tabulation([1, 2, 3, 0, 2]))
