"""
Problem description: 
---------
You are given an array 'arr' of size 'n'. It contains an even number of occurances for all numbers except two numbers.
Find those two numbers hwich have odd occurances and return in decreasing order.
Example:
Input: arr = [2,4,1,3,2,4]
Output: [3,1]
"""
from ast import List


def two_numbers_with_odd_occurances(arr: List[int]) -> List[int]:
    x = 0
    for num in arr:
        x ^= num
    # Get one set bit in the x. We get
    #  rightmost set bit in the following
    #  line as it is easy to get
    # If we bitwise AND a number with its negative counterpart, we get rightmost set bit. (just an observation based property, do remember).
    set_bit = x & ~(x - 1)
    one, two = 0, 0
    for num in arr:
        if num & set_bit:
            one ^= num
        else:
            two ^= num

    return [one, two] if one > two else [two, one]


if __name__ == '__main__':
    ex1, ex2 = [], []
    two_numbers_with_odd_occurances()
