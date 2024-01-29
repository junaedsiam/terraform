"""
Problem URL: https://leetcode.com/problems/coin-change-ii/description/
---------

Problem Description:
---------


"""
from typing import List


def coin_change_recursive(amount: int, coins: List[int]) -> int:
    # Time complexity: O(2  ^ n)
    # Space complexity: O(amount * n)
    def solve(i, left):
        if i == 0:
            if left == 0 or left % coins[i] == 0:
                return 1
            return 0

        not_pick = solve(i - 1, left)
        pick = 0
        if coins[i] <= left:
            pick = solve(i, left - coins[i])

        return pick + not_pick

    return solve(len(coins) - 1, amount)


def coin_change_memo(amount: int, coins: List[int]) -> int:
    # Time complexity: O(amount  * n)
    # Space complexity: O(amount * n)
    def solve(i, left, dp):
        if i == 0:
            if left == 0 or left % coins[0] == 0:
                return 1
            return 0
        if dp[i][left] != -1:
            return dp[i][left]
        not_pick = solve(i - 1, left, dp)
        pick = 0
        if coins[i] <= left:
            pick = solve(i, left - coins[i], dp)

        dp[i][left] = pick + not_pick
        return dp[i][left]

    n = len(coins)
    dp = [[-1] * (amount + 1) for _ in range(n)]
    return solve(n - 1, amount, dp)


def coin_change_tabulation(amount, coins):
    # Time complexity: O(amount * n)
    # Space complexity: O(amount * n)
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(coins[0], amount + 1):
        if i % coins[0] == 0:
            dp[0][i] = 1

    for i in range(1, n):
        for j in range(0, amount + 1):
            not_pick = dp[i - 1][j]
            pick = 0

            if coins[i] <= j:
                pick = dp[i][j - coins[i]]

            dp[i][j] = pick + not_pick

    return dp[n - 1][amount]


def coin_change_spaceop(amount, coins):
    # Time complexity: O(amount * n)
    # Space complexity: O(amount)
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(coins[0], amount + 1):
        if i % coins[0] == 0:
            dp[i] = 1

    for i in range(1, n):
        for j in range(0, amount + 1):
            not_pick = dp[j]
            pick = 0

            if coins[i] <= j:
                pick = dp[j - coins[i]]

            dp[j] = pick + not_pick

    return dp[amount]


if __name__ == '__main__':
    print(coin_change_spaceop(5, [1, 2, 5]))
