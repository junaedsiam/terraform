"""
Problem URL: https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945
---------

Problem Description:
---------
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 
Example 2:

Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Your Task:
Complete the function knapSack() which takes maximum capacity W, weight array wt[], value array val[], and the number of items n as a parameter and returns the maximum possible value you can get.

Expected Time Complexity: O(N*W).
Expected Auxiliary Space: O(N*W)

Constraints:
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000

"""


def zero_one_knapsack_memo(n, limit, wt, val):
    # Time complexity: O(n * limit)
    # Space complexity: O(n * limit) + O(n)
    def solve(i, limit, wt, val, dp):
        if i == 0:
            if limit >= wt[0]:
                return val[0]
            return 0

        if dp[i][limit] != -1:
            return dp[i][limit]

        not_pick = solve(i - 1, limit, wt, val, dp)

        pick = float('-inf')

        if wt[i] <= limit:
            pick = val[i] + solve(i - 1, limit - wt[i], wt, val, dp)

        dp[i][limit] = max(pick, not_pick)

        return dp[i][limit]

    dp = [[-1] * (limit + 1) for _ in range(n)]

    return solve(n - 1, limit, wt, val, dp)


def zero_one_knapsack_tabulation(n, limit, wt, val):
    # Time complexity: O(n * limit)
    # Space complexity: O(n * limit)
    dp = [[0] * (limit + 1) for _ in range(n)]

    for i in range(wt[0], limit + 1):
        dp[0][i] = val[0]

    for i in range(1, n):
        for j in range(limit + 1):
            not_pick = dp[i - 1][j]
            pick = float('-inf')

            if j >= wt[i]:
                pick = val[i] + dp[i - 1][j - wt[i]]

            dp[i][j] = max(pick, not_pick)

    return dp[n - 1][limit]


def zero_one_knapsack_space_op(n, limit, wt, val):
    # Time complexity: O(n * limit)
    # Space complexity: O(limit)
    dp = [0] * (limit + 1)
    # Base condition
    for i in range(wt[0], limit + 1):
        dp[i] = val[0]

    for i in range(1, n):
        tmp = [0] * (limit + 1)
        for j in range(limit + 1):
            not_pick = dp[j]
            pick = float('-inf')

            if j >= wt[i]:
                pick = val[i] + dp[j - wt[i]]

            tmp[j] = max(pick, not_pick)

        dp = tmp

    return dp[limit]


if __name__ == '__main__':
    print(zero_one_knapsack_tabulation(3, 4, [4, 5, 1], [1, 2, 3]))
