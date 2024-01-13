"""
Problem URL: https://www.codingninjas.com/studio/problems/minimal-cost_8180930
---------

Problem Description:
---------
This is a follow-up question to “Frog Jump” discussed in the previous article. In the previous question, the frog was allowed to jump either one or two steps at a time. In this question, the frog is allowed to jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.

"""


def frog_jump_k_distance_memo(n, k, heights):
    # memoization
    # Time complexity:O(n * k)
    # Space complexity: O(N)
    def solve(n, k, heights, dp):
        if n == 0:
            return 0

        if dp[n] != -1:
            return dp[n]

        res = float('inf')

        for i in range(1, k + 1):
            if n - i >= 0:
                curr = solve(n - i, k, heights, dp) + \
                    abs(heights[n] - heights[n - i])
                res = min(curr, res)
            dp[n] = res

        return res

    dp = [-1] * n
    return solve(n - 1, k, heights, dp)


def frog_jump_k_distance_tabulation(n, k, heights):
    # Tabulation
    # Time complexity: O(n * k)
    # Space complexity: O(n)
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] +
                            abs(heights[i] - heights[i - j]))

    return dp[n - 1]


if __name__ == '__main__':
    func = frog_jump_k_distance_tabulation
    print(func(3, 1, [2, 5, 2]))
