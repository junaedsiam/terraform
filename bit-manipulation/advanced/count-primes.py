"""
Problem description: (Sieve of Eratosthenes)
---------
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""


def count_primes(num):
    primes = [1 for _ in range(num)]
    p = 2
    while p * p < num:
        if primes[p]:
            for idx in range(p * p, num, p):
                primes[idx] = 0
        p += 1

    return sum([primes[n] for n in range(2, num)])


if __name__ == '__main__':
    print(count_primes(10))
