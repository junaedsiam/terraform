"""
Problem URL: https://www.codingninjas.com/studio/problems/ninja%E2%80%99s-training_3621003 
---------

Problem Description:
---------
Ninja is planing this ‘N’ days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?

You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 100000.
1 <= values of POINTS arrays <= 100 .

Time limit: 1 sec
Sample Input 1:
2
3
1 2 5 
3 1 1
3 3 3
3
10 40 70
20 50 80
30 60 90
Sample Output 1:
11
210

"""


from typing import List


def ninjas_training_recursive(n: int, points: List[List[int]]) -> int:
    # Recursion
    # Time complexity: O(2 ^ n) -- throws TLE
    # Space complexity: O(n) -- Recursion Stack
    def solve(day: int, last: int, points: List[List[int]]) -> int:
        if day == 0:
            res_max = 0

            for i in range(3):
                if i != last:
                    res_max = max(res_max, points[day][i])

            return res_max
            # Following line also works, but this is not as readable
            # return max([points[day][i] for i in range(2) if i!=last])

        res_max = 0

        for i in range(3):
            if i != last:
                res_max = max(res_max, points[day]
                              [i] + solve(day - 1, i, points))

        return res_max

    return solve(n - 1, 3, points)


def ninja_training_memo(n: int, points: List[List[int]]) -> int:
    # Time complexity: O(n * 4)
    # Space complexity: O(n) -- Recursion Stack
    def solve(day: int, last: int, points: List[List[int]], dp: List[List[int]]) -> int:

        if dp[day][last] != -1:
            return dp[day][last]

        if day == 0:
            res_max = 0

            for i in range(3):
                if i != last:
                    res_max = max(res_max, points[day][i])

            dp[day][last] = res_max
            return res_max

        res_max = 0

        for i in range(3):
            if i != last:
                res_max = max(res_max, points[day]
                              [i] + solve(day - 1, i, points, dp))
        dp[day][last] = res_max
        return res_max

    dp = [[-1] * 4 for _ in range(n)]
    return solve(n - 1, 3, points, dp)


def ninja_training_tabulation(n: int, points: List[List[int]]) -> int:
    # Tabulation: Bottom up
    # Time complexity: O(n)
    # Space complexity: O(n)
    dp = [[0] * 4 for _ in range(n)]

    for i in range(4):
        dp[0][i] = max([points[0][j] for j in range(3) if i != j])

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    dp[day][last] = max(
                        dp[day][last], points[day][task] + dp[day - 1][task])
    # print(dp)
    return dp[n - 1][3]


def ninja_training_spaceop(n: int, points: List[List[int]]) -> int:
    # Space optimization
    # Time complexity: O(n)
    # Space complexity: O(1)
    dp = [0 for _ in range(4)]

    for i in range(4):
        dp[i] = max([points[0][j] for j in range(3) if i != j])

    for day in range(1, n):
        tmp = [0 for _ in range(4)]
        for last in range(4):
            tmp[last] = 0
            for task in range(3):
                if task != last:
                    tmp[last] = max(
                        tmp[last], points[day][task] + dp[task])
        dp = tmp

    return tmp[3]


if __name__ == '__main__':
    func = ninja_training_spaceop
    ex = [[87, 64, 14], [44, 55, 75], [30, 4, 25], [65, 42, 85], [51, 85, 4], [47, 72, 92], [15, 13, 58], [45, 4, 14], [67, 89, 27], [22, 11, 7], [81, 31, 1], [97, 98, 61], [52, 28, 86], [98, 26, 5], [99, 93, 81], [22, 44, 42], [39, 70, 40], [14, 95, 16], [16, 6, 25], [85, 76, 2], [17, 55, 10], [57, 85, 100], [52, 52, 41], [40, 15, 72], [86, 50, 30], [40, 19, 43], [82, 62, 39], [30, 89, 69], [74, 81, 86], [9, 18, 88], [59, 78, 34], [85, 2, 59], [4, 78, 8], [17, 94, 76], [46, 60, 29], [72, 72, 47], [43, 66, 32], [53, 30, 46], [98, 89, 61], [64, 18, 38], [81, 65, 33], [14, 42, 17], [14, 79, 76], [8, 46, 29], [19, 92, 62], [36, 2, 76], [69, 71, 87], [4, 82, 31], [20, 34, 7], [
        69, 45, 90], [33, 30, 66], [48, 70, 56], [9, 95, 11], [83, 92, 34], [86, 72, 47], [76, 91, 84], [52, 36, 5], [78, 47, 97], [28, 39, 1], [18, 46, 10], [66, 74, 2], [44, 64, 84], [8, 95, 89], [89, 38, 79], [43, 84, 5], [12, 13, 22], [3, 98, 97], [55, 60, 94], [10, 67, 42], [30, 55, 83], [59, 49, 50], [21, 58, 18], [30, 67, 81], [15, 99, 67], [11, 58, 74], [73, 40, 17], [91, 72, 38], [40, 37, 63], [39, 52, 99], [85, 79, 67], [25, 1, 21], [48, 98, 29], [34, 18, 99], [24, 3, 52], [84, 38, 100], [89, 93, 85], [13, 39, 47], [53, 44, 54], [6, 37, 67], [65, 31, 14], [14, 59, 88], [92, 44, 45], [93, 44, 38], [36, 53, 76], [44, 50, 41], [44, 44, 13], [62, 44, 98], [26, 31, 60], [97, 85, 80]]

    print(func(len(ex), ex))
    # print(ninja_training_spaceop(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
