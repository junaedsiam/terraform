"""
Problem URL: https://leetcode.com/problems/coin-change/
---------

Problem Description:
---------
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""


def coin_change_recursive(coins, amount):
    # Time complexity: O(2 ^ n)
    # Space complexity: O(n)
    def solve(idx, amount, coins):
        if idx == 0:
            if amount % coins[0] == 0:
                return amount // coins[idx]
            return 1e9

        not_pick = 0 + solve(idx - 1, amount, coins)
        pick = 1e9

        if coins[idx] <= amount:
            pick = 1 + solve(idx, amount - coins[idx], coins)

        return min(pick, not_pick)

    res = solve(len(coins) - 1, amount, coins)
    return res if res != 1e9 else -1


def coin_change_memo(coins, amount):
    # Time complexity: O(n * amount)
    # Space complexity: O(n * amount) + O(n)

    def solve(idx, amount, coins, dp):
        if idx == 0:
            if amount % coins[0] == 0:
                return amount // coins[idx]
            return 1e9

        if dp[idx][amount] != -1:
            return dp[idx][amount]

        not_pick = 0 + solve(idx - 1, amount, coins, dp)
        pick = 1e9

        if coins[idx] <= amount:
            pick = 1 + solve(idx, amount - coins[idx], coins, dp)

        dp[idx][amount] = min(pick, not_pick)
        return dp[idx][amount]

    n = len(coins)
    dp = [[-1] * (amount + 1) for _ in range(n)]
    res = solve(n - 1, amount, coins, dp)
    return res if res != 1e9 else -1


def coin_change_tabulation(coins, amount):
    # Time complexity: O(n * amount)
    # Space complexity: O(n * amount)

    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]

    for i in range(amount + 1):
        if i % coins[0] == 0:
            dp[0][i] = i // coins[0]
        else:
            dp[0][i] = 1e9

    for i in range(1, n):
        for j in range(amount + 1):
            not_pick = 0 + dp[i - 1][j]
            pick = 1e9
            if coins[i] <= j:
                pick = 1 + dp[i][j - coins[i]]
            dp[i][j] = min(pick, not_pick)

    return dp[n - 1][amount] if dp[n - 1][amount] != 1e9 else -1


def coin_change_spaceop(coins, amount):
    # Time complexity: O(n * amount)
    # Space complexity: O(amount)
    n = len(coins)
    dp = [0] * (amount + 1)

    for i in range(amount + 1):
        if i % coins[0] == 0:
            dp[i] = i // coins[0]
        else:
            dp[i] = 1e9

    for i in range(1, n):
        for j in range(amount + 1):
            not_pick = 0 + dp[j]
            pick = 1e9
            if coins[i] <= j:
                pick = 1 + dp[j - coins[i]]
            dp[j] = min(pick, not_pick)

    return dp[amount] if dp[amount] != 1e9 else -1


if __name__ == '__main__':
    print(coin_change_spaceop([1, 2, 5], 11))
