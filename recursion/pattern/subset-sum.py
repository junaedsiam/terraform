"""
Problem description: 
---------
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Examples:

Example 1:

Input: N = 3, arr[] = {5,2,1}

Output: 0,1,2,3,5,6,7,8

Explanation: We have to find all the subset's sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8


Input: N=3,arr[]= {3,1,2}

Output: 0,1,2,3,3,4,5,6

Explanation: We have to find all the subset's sum and print them.in this case the generated subsets are [ [], [1], [2], [2,1], [3], [3,1], [3,2]. [3,2,1],so the sums we get will be  0,1,2,3,3,4,5,6

"""


def subset_sum_iterative(nums):
    # Iterative approach
    # Time complexity: O(2 ^ n)
    # 2 ^ 3 = 8
    # in binary - 1 << 3 -> 100 -> 8
    # 0 -> 000 -> [] # 1 -> 001 -> [2] # 2 -> 010 -> [1] # 3 -> 011 -> [1,2] # 4 -> 100 -> [3] .....
    n = len(nums)
    res = []
    for num in range(1 << n):
        sum = 0
        for i in range(num):
            if num & (1 << i):
                sum += nums[i]
        res.append(sum)
    res.sort()
    return res


def subset_sum_recurse(nums):
    # Time complexity: O ( 2 ^ n)
    n = len(nums)
    res = []

    def solve(idx, sum):
        if idx == len(nums):
            res.append(sum)
            return
        solve(idx + 1, sum+nums[idx])  # Pick
        solve(idx + 1, sum)  # Not Pick

    solve(0, 0)
    res.sort()

    return res


if __name__ == '__main__':
    func = subset_sum_recurse
    ex_1, ex_2 = [5, 2, 1], [3, 1, 2]
    print(func(ex_1))
    print(func(ex_2))
