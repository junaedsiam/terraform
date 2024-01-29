"""
Problem URL: https://www.codingninjas.com/studio/problems/rod-cutting-problem_800284
---------

Problem Description:
---------
Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost associated with it. Determine the maximum cost obtained by cutting the rod and selling its pieces.

Note:
1. The sizes will range from 1 to ‘N’ and will be integers.

2. The sum of the pieces cut should be equal to ‘N’.

3. Consider 1-based indexing.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= A[i] <= 100

Where ‘T’ is the total number of test cases, ‘N’ denotes the length of the rod, and A[i] is the cost of sub-length.


"""


def cut_rod_memo(n, prices):
    # Time complexity: O ( n ^ 2)
    # Space complexity: O ( n ^ 2) + O(n)

    def solve(i, limit):
        if i == 0:
            return limit * prices[0]

        not_pick = solve(i - 1, limit)
        pick = -1e9
        rodLength = i + 1
        if rodLength <= limit:
            pick = prices[i] + solve(i, limit - rodLength)

        return max(pick, not_pick)

    return solve(n - 1, n)


def cut_rod_tabulation(n, prices):
    # Time complexity: O ( n ^ 2)
    # Space complexity: O ( n ^ 2)
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(n + 1):
        dp[0][i] = i * prices[0]

    for i in range(1, n):
        for j in range(0, n + 1):
            not_pick = dp[i - 1][j]
            pick = -1e9

            if i + 1 <= j:
                pick = prices[i] + dp[i][j - i - 1]

            dp[i][j] = max(pick, not_pick)

    return dp[n - 1][n]


if __name__ == '__main__':
    print(cut_rod_tabulation(5, [2, 5, 7, 8, 10]))
