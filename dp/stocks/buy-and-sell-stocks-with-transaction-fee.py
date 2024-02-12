"""
Problem URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
---------

Problem Description:
---------
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104

"""


def buy_and_sell_stocks_with_transaction_fee(prices, fee):
    '''
    This is similar to all the other stock related problems.
    Only difference is the added transaction fee.
    Upon sell we can deduct the transaction fee. And thats the only 
    thing we have to do extra for this problem 
    '''
    # Time complexity: O(2n)
    # Space complexity: O(2n)
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 2)]

    for i in range(n - 1, -1, -1):
        for j in range(2):
            if j:
                dp[i][j] = max(-prices[i] + dp[i + 1][0], dp[i + 1][1])
            else:
                dp[i][j] = max(prices[i] + dp[i + 1][1] - fee, dp[i + 1][0])

    return dp[0][1]


if __name__ == '__main__':
    print(buy_and_sell_stocks_with_transaction_fee([1, 3, 2, 8, 4, 9], 2))
