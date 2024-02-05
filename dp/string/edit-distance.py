"""
Problem URL: https://leetcode.com/problems/edit-distance/
---------

Problem Description:
---------

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


def min_distance_recursive(word1, word2):
    # Time complexity: O(3 ^ m * 3 ^ n)
    # Space complexity: O(m + n)
    def solve(i, j, word1, word2):
        # base case
        # i reached negative index
        if i < 0:
            # w1 = horse, w2 = ros i==-1 meaning w1 curr state = ""
            # and for instance lets assume w2 is at 1st index.
            # meaning remaining w2 is "ro". So to make from "" to "ro"
            # we need two insert operation, which is j + 1
            return j + 1

        if j < 0:
            # so if w2 = "", w1 = "hor" meaning i is at 2nd index
            # number of operations to make w1 to w2 is 3 which is i + 1
            return i + 1

        if word1[i] == word2[j]:
            return solve(i - 1, j - 1, word1, word2)
        else:
            # insert i
            ires = 1 + solve(i, j - 1, word1, word2)
            # delete i
            dres = 1 + solve(i - 1, j, word1, word2)
            # replace i
            rres = 1 + solve(i - 1, j - 1, word1, word2)

            return min(ires, dres, rres)

    m = len(word1)
    n = len(word2)

    return solve(m - 1, n - 1, word1, word2)


def min_distance_memo(word1, word2):
    # Time complexity: O(m * n)
    # Space complexity: O(m * n) + O( m + n )
    def solve(i, j, word1, word2, dp):
        if i < 0:
            # see explanation from min_distance_recursive
            return j + 1
        if j < 0:
            # see explanation from min_distance_recursive
            return i + 1

        if dp[i][j] != -1:
            return dp[i][j]

        if word1[i] == word2[j]:
            dp[i][j] = solve(i - 1, j - 1, word1, word2, dp)
            return dp[i][j]
        else:
            # insert i
            ires = 1 + solve(i, j - 1, word1, word2, dp)
            # delete i
            dres = 1 + solve(i - 1, j, word1, word2, dp)
            # replace i
            rres = 1 + solve(i - 1, j - 1, word1, word2, dp)

            dp[i][j] = min(ires, dres, rres)

            return dp[i][j]

    m = len(word1)
    n = len(word2)
    dp = [[-1] * n for _ in range(m)]

    return solve(m - 1, n - 1, word1, word2, dp)


def min_distance_tabulation(word1, word2):
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    # tabulation needs right shift in index by one
    # as we are dealing with -1 as base cases
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for j in range(1, n + 1):
        # So for one right shift we can set only "j" instead of "j + 1"
        dp[0][j] = j
    for i in range(1, m + 1):
        # Similarly for i
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                ires = 1 + dp[i][j - 1]
                dres = 1 + dp[i - 1][j]
                rres = 1 + dp[i - 1][j - 1]
                dp[i][j] = min(ires, dres, rres)

    return dp[m][n]


if __name__ == '__main__':
    print(min_distance_tabulation("intention", "execution"))
