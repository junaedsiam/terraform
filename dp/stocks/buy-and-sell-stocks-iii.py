"""
Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
---------

Problem Description:
---------

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""


'''
# I got really confused by the description of this problem.
# At first I did not get the difference between this and "Best Time 
# to Buy and Sell Stock II". After spending sometime I found it.
# A transaction means buying a stock first and then selling it.
# So atmost two transactions mean 2 (buy + sell) atmost
# But the order should be buy -> sell -> buy -> sell
'''




from typing import List
def max_profit_recursive(prices: List[int]) -> int:
    # Time Complexity: O( 2 ^ n)
    # Space Complexity: O(1)
    def solve(i, buy, cap, prices):
        # base case
        if i == len(prices) or not cap:
            return 0
        take, not_take = None, None
        # buy = 0 meaning you must buy, you cannot sell
        if not buy:
            take = -prices[i] + solve(i + 1, 1, cap, prices)
            not_take = solve(i + 1, 0, cap, prices)
        # buy= 1 meaning you must sell, you cannot buy
        else:
            take = prices[i]+solve(i + 1, 0, cap - 1, prices)
            not_take = solve(i + 1, 1, cap, prices)
        return max(take, not_take)

    return solve(0, 0, 2, prices)


def max_profit_memo(prices: List[int]) -> int:
    # Time Complexity: O(n * 2 * 3) -> O(6n)
    # Space Complexity: O(6n) + O(n)
    def solve(i, buy, cap, prices, dp):
        # base case
        if i == len(prices) or not cap:
            return 0

        if dp[i][buy][cap] != -1:
            return dp[i][buy][cap]

        take, not_take = None, None
        # buy = 0 meaning you must buy, you cannot sell
        if not buy:
            take = -prices[i] + solve(i + 1, 1, cap, prices, dp)
            not_take = solve(i + 1, 0, cap, prices, dp)
        # buy= 1 meaning you must sell, you cannot buy
        else:
            take = prices[i] + solve(i + 1, 0, cap - 1, prices, dp)
            not_take = solve(i + 1, 1, cap, prices, dp)
        dp[i][buy][cap] = max(take, not_take)

        return dp[i][buy][cap]

    n = len(prices)
    dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

    return solve(0, 0, 2, prices, dp)


def max_profit_tabulation(prices: List[int]) -> int:
    # Time Complexity: O(n * 2 * 3) -> O(6n)
    # Space Complexity: O(6n)
    n = len(prices)
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(2):
            for cap in range(1, 3):
                take, not_take = None, None
                if j == 0:
                    take = -prices[i] + dp[i + 1][1][cap]
                    not_take = dp[i + 1][0][cap]
                else:
                    take = prices[i] + dp[i + 1][0][cap - 1]
                    not_take = dp[i + 1][1][cap]

                dp[i][j][cap] = max(take, not_take)

    return dp[0][0][2]


def max_profit_tabulation_with_k(k: int, prices: List[int]) -> int:
    # Time Complexity: O(n * 2 * 3) -> O(6n)
    # Space Complexity: O(6n)
    n = len(prices)
    dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for j in range(2):
            for cap in range(1, k + 1):
                take, not_take = None, None
                if j == 0:
                    take = -prices[i] + dp[i + 1][1][cap]
                    not_take = dp[i + 1][0][cap]
                else:
                    take = prices[i] + dp[i + 1][0][cap - 1]
                    not_take = dp[i + 1][1][cap]

                dp[i][j][cap] = max(take, not_take)

    return dp[0][0][k]


if __name__ == '__main__':
    print(max_profit_tabulation_with_k(2, [3, 2, 6, 5, 0, 3]))
