"""
Problem description: 
---------
You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division's result is less than or equal to the given threshold value.
-------------
Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.
-------------
Example 2:
Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
Result: 2
Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.
"""
import math


def sum_of_quotient(nums, divisor):
    sum = 0
    for num in nums:
        sum += math.ceil(num / divisor)
    return sum


def find_the_smallest_divisor(nums, limit):
    # Time complexity: O(n log(m))
    low = 1
    n = len(nums)
    high = max(nums)
    res = n
    while low <= high:
        # take the mid, and get the sum of ceil quotient
        mid = (low + high) // 2
        q_sum = sum_of_quotient(nums, mid)
        if q_sum <= limit:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


if __name__ == '__main__':
    ex_1, ex_2 = ([1, 2, 3, 4, 5], 8), ([8, 4, 2, 3], 10)
    print(find_the_smallest_divisor(ex_1[0], ex_1[1]))
    print(find_the_smallest_divisor(ex_2[0], ex_2[1]))
