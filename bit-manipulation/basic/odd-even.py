"""
Problem description: 
---------
You are given an integer 'N'. Return 'odd' if the given number 'N' is odd, else return 'even'
N=5, Output: odd
N=4, Output: even
"""


def odd_even(n):
    return 'odd' if n & 1 else 'even'


if __name__ == '__main__':
    print(odd_even(4))
    print(odd_even(5))
