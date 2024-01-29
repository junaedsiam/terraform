"""
Problem URL: https://www.codingninjas.com/studio/problems/unbounded-knapsack_1215029
---------

Problem Description:
---------
You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.



You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed to take one item multiple times.



Example:
Input: 
'n' = 3, 'w' = 10, 
'profit' = [5, 11, 13]
'weight' = [2, 4, 6]

Output: 27

Explanation:
We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 = 11 + 11 + 5 = 27. Therefore maximum profit = 27.

"""
from typing import List


def unbounded_knapsack_memo(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    # Time complexity: O(n * w)
    # Space complexity: O(n * w)
    def solve(i, limit, profit, weight, dp):
        if i == 0:
            return (limit // weight[0]) * profit[0]

        if dp[i][limit] != -1:
            return dp[i][limit]

        not_pick = solve(i - 1, limit, profit, weight, dp)
        pick = -1e9
        if limit >= weight[i]:
            pick = profit[i] + solve(i, limit - weight[i], profit, weight, dp)

        dp[i][limit] = max(pick, not_pick)
        return dp[i][limit]

    dp = [[-1] * (w + 1) for _ in range(n)]
    return solve(n - 1, w, profit, weight, dp)


def unbounded_knapsack_tabulation(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    # Time complexity: O(n * w)
    # Space complexity: O(n * w)
    dp = [[0] * (w + 1) for _ in range(n)]

    for i in range(w + 1):
        dp[0][i] = (i // weight[0]) * profit[0]

    for i in range(1, n):
        for j in range(0, w + 1):
            not_pick = dp[i - 1][j]
            pick = -1e9
            if j >= weight[i]:
                pick = profit[i] + dp[i][j - weight[i]]

            dp[i][j] = max(pick, not_pick)

    return dp[n - 1][w]


if __name__ == '__main__':
    print(unbounded_knapsack_tabulation(3, 10, [5, 11, 3], [2, 4, 6]))
