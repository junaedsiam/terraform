"""
Problem URL: https://www.codingninjas.com/studio/problems/subset-sum-equal-to-k_1550954
---------

Problem Description:
---------
Problem statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Time Limit: 1 sec
Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.

"""

from os import *
from sys import *
from collections import *
from math import *


def subset_sum_equal_k_recurse(n, k, arr):
    def solve(idx, target):
        if target == 0:
            return True

        if idx == 0:
            return arr[idx] == target

        not_pick = solve(idx - 1, target)
        pick = False

        if target >= arr[idx]:
            pick = solve(idx - 1, target - arr[idx])

        return not_pick or pick

    return solve(n - 1, k)


def subset_sum_equal_k_memo(n, k, arr):

    def solve(idx, target, dp):
        if target == 0:
            return True

        if idx == 0:
            return arr[idx] == target

        if dp[idx][target] != -1:
            return dp[idx][target]

        not_pick = solve(idx - 1, target, dp)
        pick = False
        if target >= arr[idx]:
            pick = solve(idx - 1, target - arr[idx], dp)

        dp[idx][target] = not_pick or pick

        return dp[idx][target]

    dp = [[-1] * (k + 1) for _ in range(n)]

    return solve(n - 1, k, dp)


def subset_sum_equal_k_tabulation(n, k, arr):

    dp = [[0] * (k + 1) for _ in range(n)]

    # Mark target 0 as true
    for i in range(n):
        dp[i][0] = True

    if arr[0] <= k:
        dp[0][arr[0]] = True

    for i in range(1, n):
        for target in range(1, k + 1):
            not_pick = dp[i - 1][target]
            pick = False
            if arr[i] <= target:
                pick = dp[i - 1][target - arr[i]]
            dp[i][target] = pick or not_pick

    return dp[n - 1][k]


if __name__ == '__main__':
    func = subset_sum_equal_k_tabulation
    print(func(5, 4, [2, 5, 1, 6, 7]))
