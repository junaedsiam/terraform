"""
Problem URL: https://www.codingninjas.com/studio/problems/matrix-chain-multiplication_624880
---------

Problem Description:
---------
Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.

You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3
10 15 20 25
Sample Output 1:
8000
Sample Output Explanation:
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000. 

"""


def matrix_chain_multiplication_recursion(p, n):
    # Recursion
    # Time Complexity: O(2 ^ n)
    # Space Complexity: O(n) # Stack space
    def f(i, j, p):
        if i == j:
            return 0

        mini = float('inf')
        for k in range(i, j):
            res = f(i, k, p) + f(k + 1, j, p) + p[i - 1] * p[k] * p[j]
            mini = min(mini, res)

        return mini

    return f(1, n - 1, p)


def matrix_chain_multiplication(arr, n):
    # Tabulation
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n ^ 2)
    # Initialize a 2D dp list with -1 values
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    # Initialize the diagonal elements of the dp table to 0
    for i in range(n):
        dp[i][i] = 0

    # Loop through the dp table to calculate the minimum number of operations
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            mini = float('inf')

            # Partitioning loop
            for k in range(i, j):
                ans = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                mini = min(mini, ans)

            dp[i][j] = mini

    # The result is stored in the top-right corner of the dp table
    return dp[1][n - 1]


if __name__ == '__main__':
    print(matrix_chain_multiplication([10, 15, 20, 25], 4))
